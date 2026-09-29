import pytest
from streamlit.testing.v1 import AppTest
from python_examples.streamlit_app.app import grade_label


@pytest.mark.unit
def test_grade_label_unit():
    assert grade_label(70) == "Pass"
    assert grade_label(69) == "Needs Improvement"


@pytest.mark.acceptance
def test_user_can_evaluate_a_score():
    at = AppTest.from_file("python_examples/streamlit_app/app.py")
    at.run()
    at.number_input[0].set_value(92)
    at.button[0].click().run()
    assert at.success[0].value == "Pass"
