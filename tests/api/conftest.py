import os

import pytest
import requests


BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8000")

TEST_EMAIL = os.getenv("TEST_EMAIL", "qaz@qaz.qaz")
TEST_PASSWORD = os.getenv("TEST_PASSWORD", "qazqaz")

SECOND_TEST_EMAIL = os.getenv(
    "SECOND_TEST_EMAIL",
    "user@example.com"
)
SECOND_TEST_PASSWORD = os.getenv(
    "SECOND_TEST_PASSWORD",
    "string"
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