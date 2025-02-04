import streamlit as st
import sqlite3

# Database setup
def setup_database():
    """
    Sets up the SQLite database and creates a table for storing guest data if it doesn't exist.
    """
    connection = sqlite3.connect("image_data1.db")
    cursor = connection.cursor()

    # Create table if it doesn't already exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS guest_data (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        dietary_preferences TEXT,
                        arrival_time TEXT,
                        departure_time TEXT,
                        preferred_language TEXT,
                        visit_purpose TEXT,
                        room_preference TEXT,
                        meals_expense REAL,
                        spa_expense REAL,
                        minibar_expense REAL,
                        notes TEXT
                      )''')
    connection.commit()
    connection.close()

# Save data to the database
def save_to_database(data):
    """
    Saves the provided data into the SQLite database.

    Args:
        data (tuple): A tuple containing all the guest details.
    """
    connection = sqlite3.connect("image_data1.db")
    cursor = connection.cursor()

    # Insert data into the table
    cursor.execute('''INSERT INTO guest_data 
                      (name, dietary_preferences, arrival_time, departure_time, preferred_language, 
                       visit_purpose, room_preference, meals_expense, spa_expense, minibar_expense, notes) 
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', data)
    connection.commit()
    connection.close()

# Main function for data entry
def display_confirmation():
    """
    Displays a confirmation message or summary of entered data to ensure accuracy and stores the data in the database.

    Returns:
        None
    """
    # Collect input data
    st.subheader("Guest Data Entry")
    name = st.text_input("Guest Name")
    dietary_preferences = st.text_input("Dietary Preferences (e.g., Vegetarian, Vegan, etc.)")
    arrival_time = st.time_input("Arrival Time")
    departure_time = st.time_input("Departure Time")
    preferred_language = st.text_input("Preferred Language")
    visit_purpose = st.selectbox("Purpose of Stay", ["Business", "Vacation", "Others"])
    room_preference = st.selectbox("Room Preferences", ["Quiet Room", "Accessibility Features", "Any"])
    meals_expense = st.number_input("Meals Expense ($)", min_value=0.0, step=0.01)
    spa_expense = st.number_input("Spa Treatments Expense ($)", min_value=0.0, step=0.01)
    minibar_expense = st.number_input("Minibar Usage Expense ($)", min_value=0.0, step=0.01)
    notes = st.text_area("Additional Notes")

    # Display confirmation and save data
    if st.button("Save and Confirm"):
        data = (
            name,
            dietary_preferences,
            str(arrival_time),
            str(departure_time),
            preferred_language,
            visit_purpose,
            room_preference,
            meals_expense,
            spa_expense,
            minibar_expense,
            notes,
        )

        # Save data to the database
        save_to_database(data)

        # Display confirmation message
        st.subheader("Confirmation of Data Entry")
        st.write(f"Name: {name}")
        st.write(f"Dietary Preferences: {dietary_preferences}")
        st.write(f"Arrival Time: {arrival_time}")
        st.write(f"Departure Time: {departure_time}")
        st.write(f"Preferred Language: {preferred_language}")
        st.write(f"Visit Purpose: {visit_purpose}")
        st.write(f"Room Preference: {room_preference}")
        st.write(f"Meals Expense: ${meals_expense}")
        st.write(f"Spa Expense: ${spa_expense}")
        st.write(f"Minibar Expense: ${minibar_expense}")
        st.write(f"Additional Notes: {notes}")
        st.success("Data successfully saved to the database!")
    else:
        st.info("Please fill out the form and press 'Save and Confirm'.")
if __name__ == "__main__":
    st.title("Function 5")
    # Set up the database
    setup_database()

    # Run the main function
    display_confirmation()
