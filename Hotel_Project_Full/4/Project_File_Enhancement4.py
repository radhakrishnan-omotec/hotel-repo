# Enhanced Python File for Notes Section
import streamlit as st

def additional_notes():
    """
    A free-text field where staff can record special requests or other important details about the guest.

    Returns:
        str: The notes entered by the staff.
    """
    # Display a subheader to introduce the additional notes section
    st.subheader("Additional Notes")
    
    # Text area for entering notes
    # Allows staff to record special requests or important guest details
    notes = st.text_area("Enter any special requests or important details about the guest.")

    # Return the notes entered by the user
    return notes

if __name__ == "__main__":
    # Collect additional notes from the user
    guest_notes = additional_notes()
    
    # Display the collected notes
    st.write("### Collected Notes")
    st.write(guest_notes)
