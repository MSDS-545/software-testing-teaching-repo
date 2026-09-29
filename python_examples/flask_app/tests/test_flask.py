import pytest
from python_examples.flask_app.app import create_app
from python_examples.flask_app.service import greeting


@pytest.mark.unit
def test_greeting_unit():
    assert greeting("Student") == "Hello, Student!"


@pytest.mark.integration
def test_greeting_route_integration():
    client = create_app().test_client()
    response = client.get("/api/greeting?name=Student")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, Student!"}


@pytest.mark.acceptance
def test_blank_name_is_explained_to_user():
    # Given a user calls the greeting endpoint without a name
    client = create_app().test_client()
    # When the request is processed
    response = client.get("/api/greeting")
    # Then the user gets a clear client error
    assert response.status_code == 400
    assert "name is required" in response.get_json()["error"]
