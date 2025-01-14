import streamlit as st
from streamlit.components.v1 import html

# Set up the page configuration
st.set_page_config(page_title="Name of Hotel", layout="centered")

# Title at the top center
st.markdown(
    "<h1 style='text-align: center;'>Name of Hotel</h1>",
    unsafe_allow_html=True
)

# Subtitle at the center
st.markdown(
    "<h2 style='text-align: center;'>Menu</h2>",
    unsafe_allow_html=True
)

# Define button actions
def handle_function_click(function_name):
    st.warning(f"Name of Hotel - {function_name}")

# Add buttons for hotel functions
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    if st.button("Hotel Function1"):
        handle_function_click("Function1")
    if st.button("Hotel Function4"):
        handle_function_click("Function4")

with col2:
    if st.button("Hotel Function2"):
        handle_function_click("Function2")
    if st.button("Hotel Function5"):
        handle_function_click("Function5")

with col3:
    if st.button("Hotel Function3"):
        handle_function_click("Function3")
    if st.button("Hotel Function6"):
        handle_function_click("Function6")

# Main Menu button at the bottom center
st.markdown("<div style='position: fixed; bottom: 30px; width: 100%; text-align: center;'>",
            unsafe_allow_html=True)
if st.button("Main Menu"):
    st.info("Returning to Main Menu")
st.markdown("</div>", unsafe_allow_html=True)
