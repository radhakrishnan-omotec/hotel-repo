import cv2
import streamlit as st
import pandas as pd
import sqlite3
import os
import numpy as np

# Load Haarcascade Face Detector
face_cascade = cv2.CascadeClassifier(r"C:\Users\saad2\Documents\GitHub\hotel-repo\Hotel_Project_Full\Main\Face_detection\haarcascade_frontalface_default.xml")

# Function to read from CSV file
def read_csv(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        st.error("CSV file not found!")
        return None

# Function to capture face data using webcam
def capture_face():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.error("Error: Webcam not detected")
        return None

    st.write("Press 'Space' to capture the face or 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Error: Could not read frame")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.imshow("Face Detection", frame)

            if cv2.waitKey(1) & 0xFF == ord(" "):  # Press Space to capture
                cap.release()
                cv2.destroyAllWindows()
                return x, y, w, h

        if cv2.waitKey(1) & 0xFF == ord("q"):  # Press 'q' to quit
            break

    cap.release()
    cv2.destroyAllWindows()
    return None

# Function to find the closest match from the CSV file
def find_closest_match(test_X, test_Y, test_Width, test_Height, csv_data):
    if csv_data is None:
        return None

    csv_data["Distance"] = np.sqrt(
        (csv_data["X"] - test_X) ** 2 +
        (csv_data["Y"] - test_Y) ** 2 +
        (csv_data["Width"] - test_Width) ** 2 +
        (csv_data["Height"] - test_Height) ** 2
    )

    closest_match = csv_data.loc[csv_data["Distance"].idxmin()]
    return closest_match

# Function to get Guest Name from SQLite database
def get_guest_name(guest_id, db_file="guests.db"): # CHANGE FOLDER NAME TO THE LOCATION WHERE THE DATABASE .DB FILE IS PLACED AND CHANGE THE NAME TO xyz.db
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM user_data WHERE id=?", (guest_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else "Guest Not Found"

# Function to open the corresponding image file
def open_guest_image(guest_name, image_folder="captured_faces/"): # CHANGE FOLDER NAME TO THE LOCATION WHERE CAPTURE IMAGES ARE PLACED
    image_path = os.path.join(image_folder, f"{guest_name}.jpg")
    if os.path.exists(image_path):
        img = cv2.imread(image_path)
        cv2.imshow(f"Guest Image - {guest_name}", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        st.error("No stored image found for this guest!")

# Streamlit Web App
def main():
    st.title("Face Recognition System")

    # Step 1: Read from CSV File
    csv_file = r"C:\Users\saad2\Documents\GitHub\hotel-repo\Hotel_Project_Full\Main\Face_detection\detected_features.csv"
    csv_data = read_csv(csv_file)

    # Step 2: Capture Face using Webcam
    if st.button("Capture Face for Recognition"):
        face_data = capture_face()
        if face_data:
            test_X, test_Y, test_Width, test_Height = face_data
            st.success(f"Captured Face: X={test_X}, Y={test_Y}, Width={test_Width}, Height={test_Height}")

            # Step 3: Find Closest Match
            match = find_closest_match(test_X, test_Y, test_Width, test_Height, csv_data)
            if match is not None:
                guest_id = match["Guest_ID"]
                guest_name = get_guest_name(guest_id)
                st.success(f"Closest Match: {guest_name}")

                # Step 4: Open Corresponding Image
                if st.button("View Guest Image"):
                    open_guest_image(guest_name)
            else:
                st.error("No matching record found.")

if __name__ == "__main__":
    main()
