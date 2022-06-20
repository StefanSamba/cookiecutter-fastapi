from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_basic_endpoint():
    response = client.get("/healthz")
    assert response.status_code == 200
