import streamlit as st
import sqlite3

# Function to collect additional guest information
def collect_additional_info():
    """
    Collects additional information from guests during check-in.

    Returns:
        tuple: Contains dietary preferences, arrival time, departure time, and preferred language.
    """
    st.subheader("Additional Guest Information")
    
    dietary_preferences = st.text_input("Dietary Preferences (e.g., Vegetarian, Vegan, etc.)")
    arrival_time = st.time_input("Arrival Time")
    departure_time = st.time_input("Departure Time")
    preferred_language = st.text_input("Preferred Language")

    return dietary_preferences, arrival_time, departure_time, preferred_language

# Function to store additional guest data into the SQLite database
def store_additional_guest_data(dietary_preferences, arrival_time, departure_time, preferred_language):
    """
    Stores the collected additional guest data into the SQLite database.

    Args:
        dietary_preferences (str): Dietary preferences of the guest.
        arrival_time (time): Arrival time of the guest.
        departure_time (time): Departure time of the guest.
        preferred_language (str): Preferred language of the guest.
    """
    # Convert the time values to strings in the format HH:MM:SS
    arrival_time_str = arrival_time.strftime('%H:%M:%S') if arrival_time else None
    departure_time_str = departure_time.strftime('%H:%M:%S') if departure_time else None

    conn = sqlite3.connect('image_data1.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS additional_guest_info (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        dietary_preferences TEXT,
                        arrival_time TEXT,
                        departure_time TEXT,
                        preferred_language TEXT)''')

    cursor.execute('''INSERT INTO additional_guest_info (dietary_preferences, arrival_time, departure_time, preferred_language)
                      VALUES (?, ?, ?, ?)''', (dietary_preferences, arrival_time_str, departure_time_str, preferred_language))
    
    conn.commit()
    conn.close()

# Function to create a submit button and save the data
def create_submit_button(dietary_preferences, arrival_time, departure_time, preferred_language):
    """
    Creates a submit button that saves the collected data to the database when clicked.
    """
    if st.button("Submit"):
        store_additional_guest_data(dietary_preferences, arrival_time, departure_time, preferred_language)
        st.success("Additional guest information has been successfully saved to the database.")

if __name__ == "__main__":
    # Collect additional guest information
    dietary, arrival, departure, language = collect_additional_info()
    
    # Create submit button
    create_submit_button(dietary, arrival, departure, language)
    
    # Optionally display the collected information before submission
    st.write("### Collected Guest Information")
    st.write(f"- Dietary Preferences: {dietary}")
    st.write(f"- Arrival Time: {arrival}")
    st.write(f"- Departure Time: {departure}")
    st.write(f"- Preferred Language: {language}")
