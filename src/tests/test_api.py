import json

from fastapi.testclient import TestClient
from src.main import app
from src.settings import AUTH_TOKEN

client = TestClient(app)


def test_secure_endpoint_with_valid_token():
    response = client.post(
        "/",
        json=test_data,
        headers={"X-API-Key": AUTH_TOKEN}
    )
    assert response.status_code == 200
    assert response.json() == {"status": "success", "message": "Email sent successfully."}

def test_secure_endpoint_with_invalid_token():
    response = client.post(
        "/",
        headers={"X-API-Key": "invalid_token"}
    )
    assert response.status_code == 403
    assert response.json() == {"detail": "Not authenticated"}
