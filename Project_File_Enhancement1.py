# Enhanced Python File for Additional Guest Information Input
import streamlit as st

def collect_additional_info():
    """
    Collects additional information from guests during check-in.

    Returns:
        tuple: Contains dietary preferences, arrival time, departure time, and preferred language.
    """
    # Display a subheader to introduce the additional guest information section
    st.subheader("Additional Guest Information")
    
    # Input field for dietary preferences
    # Allows the guest to specify their dietary restrictions or preferences
    dietary_preferences = st.text_input("Dietary Preferences (e.g., Vegetarian, Vegan, etc.)")
    
    # Input field for arrival time
    # Allows the guest to specify their expected arrival time
    arrival_time = st.time_input("Arrival Time")
    
    # Input field for departure time
    # Allows the guest to specify their expected departure time
    departure_time = st.time_input("Departure Time")
    
    # Input field for preferred language
    # Allows the guest to specify their preferred language for communication
    preferred_language = st.text_input("Preferred Language")

    # Return the collected information as a tuple
    return dietary_preferences, arrival_time, departure_time, preferred_language

if __name__ == "__main__":
    # Run the function to collect additional guest information
    dietary, arrival, departure, language = collect_additional_info()
    
    # Display the collected guest details in a structured format
    st.write("### Collected Guest Information")
    st.write(f"- Dietary Preferences: {dietary}")
    st.write(f"- Arrival Time: {arrival}")
    st.write(f"- Departure Time: {departure}")
    st.write(f"- Preferred Language: {language}")
