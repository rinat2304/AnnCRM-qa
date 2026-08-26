import pytest
import requests


BASE_URL = "http://127.0.0.1:8000"


@pytest.fixture
def auth_token():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        data={
            "username": "qaz@qaz.qaz",
            "password": "qazqaz"
        }
    )

    assert response.status_code == 200

    return response.json()["access_token"]