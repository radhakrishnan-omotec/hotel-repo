# Enhanced Python File for Additional Guest Information Input
import streamlit as st
def collect_visit_purpose():
    """
    Collects information about the guests purpose of stay and specific preferences.

    Returns:
        tuple: Contains purpose of stay and room preference.
    """
    # Display a subheader to introduce the guest visit purpose section
    st.subheader("Guest Visit Purpose and Preferences")
    
    # Dropdown to select the purpose of stay
    # Helps staff understand whether the guest is visiting for business, vacation, or other reasons
    visit_purpose = st.selectbox("Purpose of Stay", ["Business", "Vacation", "Others"])
    
    # Dropdown to select room preferences
    # Allows guests to specify their preference for quiet rooms, accessibility features, or no specific preference
    room_preference = st.selectbox("Room Preferences", ["Quiet Room", "Accessibility Features", "Any"])

    # Return the collected information as a tuple
    return visit_purpose, room_preference

if __name__ == "__main__":
    # Run the functions to collect guest information
    visit_purpose, room_preference = collect_visit_purpose()  
    st.write("### Guest Visit Purpose and Preferences")
    st.write(f"- Purpose of Stay: {visit_purpose}")
    st.write(f"- Room Preferences: {room_preference}")