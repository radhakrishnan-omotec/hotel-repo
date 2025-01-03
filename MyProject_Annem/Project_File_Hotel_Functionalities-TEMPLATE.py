import streamlit as st
import subprocess

# Set the title of the homepage
st.title("ANNEM SAAD PROJECT NAME")

# Add a section for functionalities
st.header("HOTEL FUNCTIONS")

# Define a function to execute Python files
def execute_script(script_name):
    try:
        subprocess.run(["python", script_name], check=True)
    except subprocess.CalledProcessError as e:
        st.error(f"Error occurred while running {script_name}: {e}")

# Create buttons for each functionality
if st.button("Run Functionality 1"):
    execute_script("Python1.py")

if st.button("Run Functionality 2"):
    execute_script("Python2.py")

if st.button("Run Functionality 3"):
    execute_script("Python3.py")

if st.button("Run Functionality 4"):
    execute_script("Python4.py")

if st.button("Run Functionality 5"):
    execute_script("Python5.py")

if st.button("Run Functionality 6"):
    execute_script("Python6.py")
