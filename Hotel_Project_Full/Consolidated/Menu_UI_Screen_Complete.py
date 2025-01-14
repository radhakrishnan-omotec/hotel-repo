import streamlit as st
import os

# Function to run a Streamlit script
def run_script(script_path):
    """Run a Streamlit script by providing its path."""
    os.system(f"streamlit run {script_path}")

# Set the page layout
st.set_page_config(page_title="Hotel Menu", layout="wide")

# Title at the top center
st.markdown("<h1 style='text-align: center;'>Name of Hotel</h1>", unsafe_allow_html=True)

# Subtitle at the center
st.markdown("<h2 style='text-align: center;'>Menu</h2>", unsafe_allow_html=True)

# Spacer for layout
st.write("\n" * 2)

# Create three columns for the function buttons
col1, col2, col3 = st.columns(3)

# Define function buttons and their respective actions
with col1:
    if st.button("Hotel Function1"):
        st.success("Name of Hotel - Function1")
        run_script("Main/main.py")
    if st.button("Hotel Function4"):
        st.success("Name of Hotel - Function4")
        run_script("3/Project_File_Enhancement3_db.py")

with col2:
    if st.button("Hotel Function2"):
        st.success("Name of Hotel - Function2")
        run_script("1/Project_File_Enhancement1_db.py")
    if st.button("Hotel Function5"):
        st.success("Name of Hotel - Function5")
        run_script("4/Project_File_Enhancement4.py")

with col3:
    if st.button("Hotel Function3"):
        st.success("Name of Hotel - Function3")
        run_script("2/Project_File_Enhancement2_db.py")
    if st.button("Hotel Function6"):
        st.success("Name of Hotel - Function6")
        run_script("5/Project_File_Enhancement5_db.py")

# Add a "Main Menu" button at the bottom center
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
if st.button("Main Menu"):
    st.info("Redirecting to Main Menu...")
st.markdown("</div>", unsafe_allow_html=True)
