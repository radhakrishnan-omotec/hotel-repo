# Enhanced Python File for Additional Guest Information Input with Database Integration
import streamlit as st
import sqlite3

# Database setup
def setup_database():
    """
    Sets up the SQLite database and creates tables for storing guest and billing data if they don't exist.
    """
    connection = sqlite3.connect("image_data1.db")
    cursor = connection.cursor()

    # Create guest_data table if it doesn't exist
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

    # Create billing_data table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS billing_data (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        meals_expense REAL,
                        spa_expense REAL,
                        minibar_expense REAL,
                        total_expense REAL
                      )''')

    connection.commit()
    connection.close()

# Save billing data to the database
def save_billing_data(data):
    """
    Saves the provided billing data into the SQLite database.

    Args:
        data (tuple): A tuple containing billing information (meals, spa, minibar, total).
    """
    connection = sqlite3.connect("image_data1.db")
    cursor = connection.cursor()

    # Insert data into the billing_data table
    cursor.execute('''INSERT INTO billing_data (meals_expense, spa_expense, minibar_expense, total_expense) 
                      VALUES (?, ?, ?, ?)''', data)
    connection.commit()
    connection.close()

# Main function for billing information input
def collect_billing_info():
    """
    Captures expenses like meals, spa treatments, minibar usage, and stores them for bill generation.

    Returns:
        tuple: Contains individual expenses for meals, spa treatments, minibar usage, and the total expense.
    """
    # Display a subheader to introduce the basic billing information section
    st.subheader("Basic Billing Information")
    
    # Input field for meals expense
    meals_expense = st.number_input("Meals Expense ($)", min_value=0.0, step=0.01)
    
    # Input field for spa treatments expense
    spa_expense = st.number_input("Spa Treatments Expense ($)", min_value=0.0, step=0.01)
    
    # Input field for minibar usage expense
    minibar_expense = st.number_input("Minibar Usage Expense ($)", min_value=0.0, step=0.01)

    # Calculate the total expenses
    total_expense = meals_expense + spa_expense + minibar_expense
    
    # Display the total expense to the user
    st.write(f"Total Expenses: ${total_expense}")

    # Return the collected billing information as a tuple
    return meals_expense, spa_expense, minibar_expense, total_expense
def create_submit_button(meals, spa, minibar, total):
    """
    Creates a submit button that saves the collected data to the database when clicked.
    """
    if st.button("Submit"):
        collect_billing_info(meals, spa, minibar, total)
        st.success("Guest information has been successfully saved to the database.")
if __name__ == "__main__":
    # Set up the database
    setup_database()

    # Collect billing information from the user
    meals, spa, minibar, total = collect_billing_info()

    # Save billing data to the database
    save_billing_data((meals, spa, minibar, total))

    # Display the collected billing information
    st.write("### Billing Information")
    st.write(f"- Meals Expense: ${meals}")
    st.write(f"- Spa Treatments Expense: ${spa}")
    st.write(f"- Minibar Usage Expense: ${minibar}")
    st.write(f"- Total Expense: ${total}")
    st.success("Billing data successfully saved to the database!")
