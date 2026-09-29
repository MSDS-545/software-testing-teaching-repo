import pytest
from fastapi.testclient import TestClient
from python_examples.flask_fastapi_shared.flask_api import create_app
from python_examples.flask_fastapi_shared.fastapi_api import app as fastapi_app


@pytest.mark.integration
def test_flask_and_fastapi_share_the_same_success_contract():
    flask_response = create_app().test_client().get("/api/greeting?name=Ada")
    fastapi_response = TestClient(fastapi_app).get("/api/greeting?name=Ada")

    assert flask_response.status_code == fastapi_response.status_code == 200
    assert flask_response.get_json() == fastapi_response.json() == {
        "message": "Hello, Ada!",
        "length": 3,
    }
