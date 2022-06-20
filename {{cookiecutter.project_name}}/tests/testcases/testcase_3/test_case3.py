from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_case_2(test_body, test_response):
    response = client.post(
        "/v1/{{cookiecutter.endpoint_name}}",
        headers={
            "accept": "application/json",
            "Content-Type": "application/json"},
        json=test_body,
    )
    assert response.status_code == 200
    assert response.json() == test_response
