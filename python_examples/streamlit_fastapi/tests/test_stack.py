import pytest
from pathlib import Path
from fastapi.testclient import TestClient
from streamlit.testing.v1 import AppTest

# Import the FastAPI application and the function being tested.
from python_examples.streamlit_fastapi.api.api import app, student_status

# Import the API client used by the Streamlit UI.
from python_examples.streamlit_fastapi.ui import api_client


# ---------------------------------------------------------
# UNIT TEST 1
# Tests the student_status() function by itself.
# No FastAPI server, HTTP request, or Streamlit UI is used.
# ---------------------------------------------------------
@pytest.mark.unit
def test_student_status_unit():
    result = student_status("Sam", 75)

    assert result["status"] == "on-track"


# ---------------------------------------------------------
# INTEGRATION TEST
# Tests the FastAPI endpoint together with the application
# logic using FastAPI's TestClient.
#
# This does NOT start a real web server.
# ---------------------------------------------------------
@pytest.mark.integration
def test_fastapi_backend_integration():
    client = TestClient(app)

    response = client.get(
        "/api/status?name=Sam&score=65"
    )

    assert response.status_code == 200
    assert response.json()["status"] == "needs-support"


# ---------------------------------------------------------
# UNIT TEST 2
# Tests api_client.fetch_status().
#
# The real HTTP request is replaced with fake_get().
# Therefore, this remains a unit test rather than an
# integration test.
# ---------------------------------------------------------
@pytest.mark.unit
def test_api_client_builds_request(monkeypatch):

    class FakeResponse:
        """Fake response returned instead of a real HTTP response."""

        def raise_for_status(self):
            pass

        def json(self):
            return {
                "name": "Sam",
                "score": 75,
                "status": "on-track",
            }

    captured = {}

    def fake_get(url, params, timeout):
        """Capture the HTTP request without sending it."""
        captured.update(
            url=url,
            params=params,
            timeout=timeout,
        )

        return FakeResponse()

    # Replace requests.get() inside api_client with our fake.
    monkeypatch.setattr(
        api_client.requests,
        "get",
        fake_get,
    )

    result = api_client.fetch_status(
        "http://api.test",
        "Sam",
        75,
    )

    assert result["status"] == "on-track"

    assert captured["params"] == {
        "name": "Sam",
        "score": 75,
    }


# ---------------------------------------------------------
# ACCEPTANCE TEST
# Tests behavior from the Streamlit user's perspective.
#
# The FastAPI call is mocked because this test is concerned
# with the UI behavior, not backend/API integration.
# ---------------------------------------------------------
@pytest.mark.acceptance
def test_streamlit_user_sees_status(monkeypatch):

    def fake_fetch_status(base_url, name, score):
        """Return a predictable API result for the UI test."""
        return {
            "name": name,
            "score": score,
            "status": "on-track",
        }

    # The Streamlit UI imports fetch_status from api_client.
    # Replace it so the test does not require a running
    # FastAPI server.
    monkeypatch.setattr(
        api_client,
        "fetch_status",
        fake_fetch_status,
    )

    # test_stack.py is located in:
    #
    # streamlit_fastapi/tests/test_stack.py
    #
    # Move up to streamlit_fastapi/ and then locate:
    #
    # ui/ui.py
    ui_file = (
        Path(__file__).resolve().parent.parent
        / "ui"
        / "ui.py"
    )

    # Load the Streamlit application.
    at = AppTest.from_file(str(ui_file))

    # Initial page load.
    at.run()

    # Simulate user input.
    at.text_input[0].set_value("Sam")
    at.number_input[0].set_value(88)

    # Simulate clicking "Check status".
    at.button[0].click().run()

    # Verify what the user sees.
    assert "Sam: on-track" in at.success[0].value