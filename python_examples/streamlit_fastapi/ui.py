import os
import streamlit as st
from python_examples.streamlit_fastapi.api_client import fetch_status

API_URL = os.getenv("STATUS_API_URL", "http://127.0.0.1:8000")

st.title("Student Status")
name = st.text_input("Name")
score = st.number_input("Score", min_value=0, max_value=100, value=70)

if st.button("Check status"):
    try:
        result = fetch_status(API_URL, name, int(score))
        st.success(f"{result['name']}: {result['status']}")
    except Exception as exc:
        st.error(f"Could not reach the API: {exc}")
