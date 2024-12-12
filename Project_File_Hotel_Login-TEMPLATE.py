import streamlit as st
import subprocess

# Set the title of the Login screen
st.title("ANNEM SAAD PROJECT NAME")

# Add a header for login details
st.header("LOGIN DETAILS")

# Define username and password
USERNAME = "annem_saad"
PASSWORD = "123"

# Input fields for username and password
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Submit button
if st.button("Submit"):
    if username == USERNAME and password == PASSWORD:
        st.success("Login Details Accepted")
        # Execute the Python1.py script
        try:
            subprocess.run(["python", "Python1.py"], check=True)
        except subprocess.CalledProcessError as e:
            st.error(f"Error occurred while running Python1.py: {e}")
    else:
        st.error("Invalid Username or Password")
