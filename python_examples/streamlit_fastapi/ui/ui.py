import os
import streamlit as st
from python_examples.streamlit_fastapi.ui.api_client import fetch_status

# URL of the FastAPI backend.
# The environment variable allows the API location to be changed
# without modifying the source code.
API_URL = os.getenv("STATUS_API_URL", "http://127.0.0.1:8000")

# Create the Streamlit page title.
st.title("Student Status")

# Collect the student's name.
name = st.text_input("Name")

# Collect the student's score.
score = st.number_input(
    "Score",
    min_value=0,
    max_value=100,
    value=70
)

# Send the information to FastAPI when the user clicks the button.
if st.button("Check status"):
    try:
        # api_client.py handles communication with FastAPI.
        result = fetch_status(API_URL, name, int(score))

        # Display the response returned by the API.
        st.success(f"{result['name']}: {result['status']}")

    except Exception as exc:
        # Display an error if the API cannot be reached.
        st.error(f"Could not reach the API: {exc}")