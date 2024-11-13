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
            database = "test.db"
            conn = create_connection(database)
            if conn is not None:
                # Create the table if it doesn't exist
                create_table(conn)

                # Example user data input
                age = st.number_input("Enter Age", min_value=0, max_value=120, step=1)
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
        st.write("Classification logic goes here...")

    name = st.text_input("Name of the person for Bill Generation")
    if st.button("Generate Bill"):
        st.write("Bill generation logic goes here...")

if __name__ == "__main__":
    main()

