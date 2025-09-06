import pytest
from src.tests.core import async_client
from src.settings import AUTH_TOKEN

USER_DATA = {"name": "test_user", "email": "test@email", "password": "12345"}


@pytest.mark.asyncio
async def test_secure_endpoint_with_valid_token(async_client):
    response = await async_client.get(
        "/",
        headers={"X-API-Key": AUTH_TOKEN}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Server is running."}


@pytest.mark.asyncio
async def test_secure_endpoint_with_invalid_token(async_client):
    response = await async_client.get(
        "/",
        headers={"X-API-Key": "invalid_token"}
    )
    assert response.status_code == 403
    assert response.json() == {"detail": "Not authenticated"}


@pytest.mark.asyncio
async def test_user_creation(async_client):
    response = await async_client.post(
        "/api/user",
        headers={"X-API-Key": AUTH_TOKEN},
        json=USER_DATA
    )

    assert response.status_code == 201
    assert response.json() == {"message": "User created!"}
