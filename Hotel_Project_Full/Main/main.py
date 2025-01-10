import numpy as np 
import pandas as pd 
import streamlit as st
import cv2
import os
import sqlite3

# Function to capture and save an image using the webcam
def capture_image(save_path):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.error("Error: Could not open webcam")
        return

    st.write("Press 'Space' to Capture")

    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Error: Could not read frame")
            break

        cv2.imshow("Webcam Feed - Press space to capture", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord(" "):
            # Save the image with a specific file name and extension
            save_file = os.path.join(save_path, "captured_image.jpg")  # Save as jpg file
            cv2.imwrite(save_file, frame)
            st.success(f"Image saved to {save_file}")
            break
        elif key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

# Function to create a connection to SQLite database
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
    except sqlite3.Error as e:
        print(e)
    return conn

# Function to create a table in the database if it doesn't already exist
def create_table(conn):
    try:
        query = '''CREATE TABLE IF NOT EXISTS user_data (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        age INTEGER,
                        email TEXT
                    );'''
        conn.execute(query)
        print("Table created successfully (if it didn't exist).")
    except sqlite3.Error as e:
        print(e)

# Function to insert data into the database
def insert_data(conn, user_data):
    try:
        query = '''INSERT INTO user_data (name, age, email) 
                   VALUES (?, ?, ?);'''
        conn.execute(query, user_data)
        conn.commit()  # Commit the transaction
        print("Data inserted successfully!")
    except sqlite3.Error as e:
        print(e)

# Main function to run the Streamlit app
def main():
    st.title("Webcam Image Capture and Database Storage")

    # Button to open the webcam and capture an image
    if st.button("Click Image"):
        save_path = r"C:\Users\saad2\Downloads\Face_detection"  # Change this to your desired folder path
        if not os.path.exists(save_path):
            os.makedirs(save_path)  # Create directory if it doesn't exist
        capture_image(save_path)

    person_name = st.text_input("Write the Name of the Customer")
    room_number = st.text_input("Write the room number of the customer")
    

    if st.button("Store in Database"):
        if person_name:
            # Connect to the SQLite database (or create it)
            database = "image_data1.db"
            conn = create_connection(database)
            if conn is not None:
                # Create the table if it doesn't exist
                create_table(conn)

                # Example user data input
                age = st.number_input("Enter Age")
                email = st.text_input("Enter Email")

                if st.button("Insert Data"):
                    user_data = (person_name, age, email)
                    insert_data(conn, user_data)

                # Close the database connection
                if conn:
                    conn.close()
                    st.success("Information stored in the database successfully!")
            else:
                st.error("Connection to database failed.")
        else:
            st.error("Please provide the name of the customer.")

    # Optional functionality to classify or generate bills
    if st.button("Classify"):
        # Define the absolute paths to the Haar cascade XML files
        face_cascade_path = r'C:\Users\saad2\Desktop\Project_Omotec\MyProject\opencv_3.4_data_haarcascades\haarcascade_frontalface_default.xml'
        eye_cascade_path = r'C:\Users\saad2\Desktop\Project_Omotec\MyProject\opencv_3.4_data_haarcascades\haarcascade_eye.xml'
        smile_cascade_path = r'C:\Users\saad2\Desktop\Project_Omotec\MyProject\opencv_3.4_data_haarcascades\haarcascade_smile.xml'

        # Check if all the files exist before loading them
        if not os.path.isfile(face_cascade_path):
            raise FileNotFoundError(f"Face cascade file not found at {face_cascade_path}")
        if not os.path.isfile(eye_cascade_path):
            raise FileNotFoundError(f"Eye cascade file not found at {eye_cascade_path}")
        if not os.path.isfile(smile_cascade_path):
            raise FileNotFoundError(f"Smile cascade file not found at {smile_cascade_path}")

        # Load the Haar cascades using absolute paths
        face_cascade = cv2.CascadeClassifier(face_cascade_path)
        eye_cascade = cv2.CascadeClassifier(eye_cascade_path)
        smile_cascade = cv2.CascadeClassifier(smile_cascade_path)

        # Initialize webcam video capture
        cap = cv2.VideoCapture(0)

        # Create a list to store the feature details
        features_list = []

        while True:
            # Read the frame from the camera
            ret, frame = cap.read()
            if not ret:
                break

            # Convert the frame to grayscale (Haar Cascades work better on grayscale images)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces in the image
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

            for (x, y, w, h) in faces:
                # Draw a rectangle around the detected face
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                # Store face features
                features_list.append(['Face', x, y, w, h])

                # Region of interest for detecting eyes and smile within the face rectangle
                roi_gray = gray[y:y + h, x:x + w]
                roi_color = frame[y:y + h, x:x + w]

                # Detect eyes within the face region
                eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=10, minSize=(15, 15))
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
                    # Store eye features relative to the face region
                    features_list.append(['Eye', x + ex, y + ey, ew, eh])

                # Detect smile within the face region
                smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.7, minNeighbors=22, minSize=(25, 25))
                for (sx, sy, sw, sh) in smiles:
                    cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)
                    # Store smile features relative to the face region
                    features_list.append(['Smile', x + sx, y + sy, sw, sh])

            # Display the resulting frame with detected features
            cv2.imshow('Face, Eyes, and Smile Detection', frame)

            # Break the loop on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the camera and close all windows
        cap.release()
        cv2.destroyAllWindows()

        # Create a DataFrame to store the features
        features_df = pd.DataFrame(features_list, columns=['Feature', 'X', 'Y', 'Width', 'Height'])

        # Save the features to a CSV file
        features_df.to_csv('detected_features.csv', index=False)
        print("Feature details saved to detected_features.csv")

        # If you prefer saving to an Excel file, use:
        features_df.to_excel('detected_features.xlsx', index=False)

    name = st.text_input("Name of the person for Bill Generation")
    if st.button("Generate Bill"):
        st.write("Bill generation logic goes here...")

if __name__ == "__main__":
    main()

