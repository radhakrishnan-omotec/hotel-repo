import streamlit as st
import sqlite3

# Function to collect guest visit purpose and preferences
def collect_visit_purpose():
    """
    Collects information about the guest's purpose of stay and specific preferences.

    Returns:
        tuple: Contains purpose of stay and room preference.
    """
    # Display a subheader to introduce the guest visit purpose section
    st.subheader("Guest Visit Purpose and Preferences")
    
    # Dropdown to select the purpose of stay
    visit_purpose = st.selectbox("Purpose of Stay", ["Business", "Vacation", "Others"])
    
    # Dropdown to select room preferences
    room_preference = st.selectbox("Room Preferences", ["Quiet Room", "Accessibility Features", "Any"])

    # Return the collected information as a tuple
    return visit_purpose, room_preference

# Function to connect to the database and store guest information
def store_guest_data(visit_purpose, room_preference):
    """
    Stores the collected guest data into the SQLite database.

    Args:
        visit_purpose (str): Purpose of stay.
        room_preference (str): Room preference.
    """
    # Connect to the SQLite database (create it if it doesn't exist)
    conn = sqlite3.connect('image_data1.db')
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS guest_info (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        visit_purpose TEXT,
                        room_preference TEXT)''')
    
    # Insert the collected guest data into the table
    cursor.execute('''INSERT INTO guest_info (visit_purpose, room_preference)
                      VALUES (?, ?)''', (visit_purpose, room_preference))
    
    # Commit the transaction and close the connection
    conn.commit()
    conn.close()
def create_submit_button(visit_purpose,room_preference):
    """
    Creates a submit button that saves the collected data to the database when clicked.
    """
    if st.button("Submit"):
        store_guest_data(visit_purpose,room_preference)
        st.success("Guest information has been successfully saved to the database.")

if __name__ == "__main__":
    # Run the functions to collect guest information
    visit_purpose, room_preference = collect_visit_purpose()  
    
    # Store the collected data in the database
    store_guest_data(visit_purpose, room_preference)
    create_submit_button(visit_purpose,room_preference)
    # Display the collected information
    st.write("### Guest Visit Purpose and Preferences")
    st.write(f"- Purpose of Stay: {visit_purpose}")
    st.write(f"- Room Preferences: {room_preference}")
    
    # Notify the user that the information has been stored
    st.success("Guest information has been successfully saved to the database.")
