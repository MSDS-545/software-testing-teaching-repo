import streamlit as st


def grade_label(score: int) -> str:
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    return "Pass" if score >= 70 else "Needs Improvement"


st.title("Score Checker")
score = st.number_input("Score", min_value=0, max_value=100, value=70)
if st.button("Evaluate"):
    st.success(grade_label(int(score)))
