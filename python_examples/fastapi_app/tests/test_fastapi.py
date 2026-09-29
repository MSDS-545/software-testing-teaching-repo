import pytest
from fastapi.testclient import TestClient
from python_examples.fastapi_app.app import app
from python_examples.fastapi_app.service import classify_score

client = TestClient(app)


@pytest.mark.unit
def test_classify_score_unit():
    assert classify_score(90) == "excellent"


@pytest.mark.integration
def test_result_endpoint_integration():
    response = client.get("/api/result/82")
    assert response.status_code == 200
    assert response.json() == {"score": 82, "classification": "satisfactory"}


@pytest.mark.acceptance
def test_invalid_score_returns_user_readable_error():
    # Given an invalid score
    # When a client requests a classification
    response = client.get("/api/result/140")
    # Then the API rejects it with an understandable reason
    assert response.status_code == 400
    assert response.json()["detail"] == "score must be between 0 and 100"
