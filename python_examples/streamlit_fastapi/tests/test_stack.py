import pytest
from fastapi.testclient import TestClient
from streamlit.testing.v1 import AppTest
from python_examples.streamlit_fastapi.api import app, student_status
from python_examples.streamlit_fastapi import api_client


@pytest.mark.unit
def test_student_status_unit():
    assert student_status("Sam", 75)["status"] == "on-track"


@pytest.mark.integration
def test_fastapi_backend_integration():
    response = TestClient(app).get("/api/status?name=Sam&score=65")
    assert response.status_code == 200
    assert response.json()["status"] == "needs-support"


@pytest.mark.unit
def test_api_client_builds_request(monkeypatch):
    class FakeResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return {"name": "Sam", "score": 75, "status": "on-track"}

    captured = {}

    def fake_get(url, params, timeout):
        captured.update(url=url, params=params, timeout=timeout)
        return FakeResponse()

    monkeypatch.setattr(api_client.requests, "get", fake_get)
    result = api_client.fetch_status("http://api.test", "Sam", 75)
    assert result["status"] == "on-track"
    assert captured["params"] == {"name": "Sam", "score": 75}


@pytest.mark.acceptance
def test_streamlit_user_sees_status(monkeypatch):
    def fake_fetch_status(base_url, name, score):
        return {"name": name, "score": score, "status": "on-track"}

    # The UI imports fetch_status from this module during AppTest execution.
    monkeypatch.setattr(api_client, "fetch_status", fake_fetch_status)

    at = AppTest.from_file("python_examples/streamlit_fastapi/ui.py")
    at.run()
    at.text_input[0].set_value("Sam")
    at.number_input[0].set_value(88)
    at.button[0].click().run()
    assert "Sam: on-track" in at.success[0].value
