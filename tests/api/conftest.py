import pytest
import requests

from config import (
    BASE_URL,
    TEST_EMAIL,
    TEST_PASSWORD,
    SECOND_TEST_EMAIL,
    SECOND_TEST_PASSWORD,
)

@pytest.fixture
def auth_token():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        data={
            "username": TEST_EMAIL,
            "password": TEST_PASSWORD,
        },
    )

    assert response.status_code == 200

    return response.json()["access_token"]


@pytest.fixture
def second_auth_token():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        data={
            "username": SECOND_TEST_EMAIL,
            "password": SECOND_TEST_PASSWORD,
        },
    )

    assert response.status_code == 200

    return response.json()["access_token"]

@pytest.fixture
def client_id(auth_token):
    client_data = {
        "name": "Authorization Test Client",
        "phone": "+79990001129",
        "email": "authorization@test.com",
    }

    response = requests.post(
        f"{BASE_URL}/clients",
        json=client_data,
        headers={
            "Authorization": f"Bearer {auth_token}"
        },
    )

    assert response.status_code == 200

    return response.json()["id"]