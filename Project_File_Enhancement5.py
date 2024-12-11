# Enhanced Python File for Confirmation Message After Data Entry
import streamlit as st

def display_confirmation(name, dietary_preferences, arrival_time, departure_time, preferred_language, visit_purpose, room_preference, meals_expense, spa_expense, minibar_expense, notes):
    """
    Displays a summary of the entered data for review and confirmation.

    Args:
        name (str): Guest's name.
        dietary_preferences (str): Dietary preferences of the guest.
        arrival_time (datetime.time): Guest's arrival time.
        departure_time (datetime.time): Guest's departure time.
        preferred_language (str): Preferred language of the guest.
        visit_purpose (str): Purpose of stay (e.g., business, vacation).
        room_preference (str): Room preference of the guest.
        meals_expense (float): Expense for meals.
        spa_expense (float): Expense for spa treatments.
        minibar_expense (float): Expense for minibar usage.
        notes (str): Additional notes about the guest.

    Returns:
        None
    """
    # Display a subheader to introduce the confirmation section
    st.subheader("Confirmation of Data Entry")

    # Display a summary of the entered data
    st.write(f"**Name:** {name}")
    st.write(f"**Dietary Preferences:** {dietary_preferences}")
    st.write(f"**Arrival Time:** {arrival_time}")
    st.write(f"**Departure Time:** {departure_time}")
    st.write(f"**Preferred Language:** {preferred_language}")
    st.write(f"**Visit Purpose:** {visit_purpose}")
    st.write(f"**Room Preference:** {room_preference}")
    st.write(f"**Meals Expense:** ${meals_expense:.2f}")
    st.write(f"**Spa Expense:** ${spa_expense:.2f}")
    st.write(f"**Minibar Expense:** ${minibar_expense:.2f}")
    st.write(f"**Additional Notes:** {notes}")

    # Confirmation button
    if st.button("Confirm and Save"):
        st.success("Data successfully saved!")
    else:
        st.warning("Please review and confirm the details.")

if __name__ == "__main__":
    # Example inputs for demonstration purposes
    guest_name = "John Doe"
    dietary_preferences = "Vegetarian"
    arrival_time = "3:00 PM"
    departure_time = "11:00 AM"
    preferred_language = "English"
    visit_purpose = "Vacation"
    room_preference = "Quiet Room"
    meals_expense = 120.50
    spa_expense = 85.75
    minibar_expense = 40.00
    notes = "Guest is celebrating an anniversary."

    # Display the confirmation message
    display_confirmation(guest_name, dietary_preferences, arrival_time, departure_time, preferred_language, visit_purpose, room_preference, meals_expense, spa_expense, minibar_expense, notes)
