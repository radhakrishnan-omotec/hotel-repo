import streamlit as st
import cv2
import os
import sqlite3

# Function to capture an image from the webcam and save it
def capture_image(save_path):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.error("Error: Could not open webcam.")
        return
    
    st.write("Press 'Space' to capture the image.")
    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Error: Could not read frame.")
            break
        
        # Display the webcam feed
        cv2.imshow("Webcam Feed - Press Space to Capture", frame)
        
        key = cv2.waitKey(1) & 0xFF
        if key == ord(' '):  # Space key to capture image
            cv2.imwrite(save_path, frame)
            st.success(f"Image saved to {save_path}")
            break
        elif key == ord('q'):  # 'q' key to quit
            break
    
    cap.release()
    cv2.destroyAllWindows()

# Function to store information in the database
def store_in_database(name, room_no, image_path):
    # Connect to the database (or create it if it doesn't exist)
    conn = sqlite3.connect('customer_data.db')
    c = conn.cursor()
    
    # Create the table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS customers
                 (name TEXT, room_no TEXT, image_path TEXT)''')
    
    # Insert the data into the table
    c.execute("INSERT INTO customers (name, room_no, image_path) VALUES (?, ?, ?)",
              (name, room_no, image_path))
    
    # Commit and close the connection
    conn.commit()
    conn.close()

def main():
    st.title("Webcam Image Capture and Database Storage")

    # Button to open the webcam and capture an image
    if st.button("Click Image"):
        save_path = r"C:\Users\saad2\Downloads\Face_detection"  # Change this to your desired folder path
        capture_image(save_path)

    person_name = st.text_input("Write the Name of the Customer")
    room_no = st.text_input("Enter the Room Number")

    if st.button("Store in Database"):
        if person_name and room_no:
            # Store the data in the database
            store_in_database(person_name, room_no, save_path)
            st.success("Information stored in the database successfully!")
        else:
            st.error("Please provide both name and room number.")
    if st.button("Classify"):
        print("Classified")
    name=st.text_input("Name of the person is")
    if st.button("Generate Bill"):
        print("Bill generated")

if __name__ == "__main__":
    main()
