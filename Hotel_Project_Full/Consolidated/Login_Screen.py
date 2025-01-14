import streamlit as st
from streamlit.components.v1 import html

# Center the content using Streamlit's layout options
st.set_page_config(layout="wide")

# Title at the top center
st.markdown("<h1 style='text-align: center;'>Name of Hotel</h1>", unsafe_allow_html=True)

# Subtitle "Login" in the center
st.markdown("<h2 style='text-align: center;'>Login</h2>", unsafe_allow_html=True)

# Create two columns to center-align the form
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Username input
    st.write("**Username**")
    username = st.text_input("", key="username")

    # Password input
    st.write("**Password**")
    password = st.text_input("", type="password", key="password")

    # Submit button
    if st.button("Submit"):
        if username == "annem" and password == "saad":
            # Generate a success pop-up message
            html('<script>alert("Welcome Annem Saad")</script>', height=0)
        else:
            # Generate an error pop-up message
            html('<script>alert("Invalid Login")</script>', height=0)
