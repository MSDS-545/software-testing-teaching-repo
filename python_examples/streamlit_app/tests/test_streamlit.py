from pathlib import Path

import pytest
from streamlit.testing.v1 import AppTest

from python_examples.streamlit_app.app import grade_label


@pytest.mark.unit
def test_grade_label_unit():
    """Unit test for the grade-label business logic."""

    assert grade_label(70) == "Pass"
    assert grade_label(69) == "Needs Improvement"


@pytest.mark.acceptance
def test_user_can_evaluate_a_score():
    """Acceptance test for the Streamlit user interface."""

    # This test file is located at:
    # python_examples/streamlit_app/tests/test_streamlit.py
    #
    # Move up from tests/ to streamlit_app/, then locate app.py.
    app_file = Path(__file__).resolve().parent.parent / "app.py"

    # Use the resolved path so the test works both locally
    # and in GitHub Actions.
    at = AppTest.from_file(str(app_file))

    # Start the Streamlit application.
    at.run()

    # Simulate a user entering a score.
    at.number_input[0].set_value(92)

    # Simulate the user clicking the button.
    at.button[0].click().run()

    # Verify the result shown to the user.
    assert at.success[0].value == "Pass"