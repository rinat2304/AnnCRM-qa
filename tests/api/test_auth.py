import requests


BASE_URL = "http://127.0.0.1:8000"


def test_login_success():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        data={
            "username": "qaz@qaz.qaz",
            "password": "qazqaz"
        }
    )

    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_invalid_password():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        data={
            "username": "qaz@qaz.qaz",
            "password": "wrong_password"
        }
    )

    assert response.status_code == 401

def test_get_clients_with_auth():
    login_response = requests.post(
        f"{BASE_URL}/auth/login",
        data={
            "username": "qaz@qaz.qaz",
            "password": "qazqaz"
        }
    )

    assert login_response.status_code == 200

    token = login_response.json()["access_token"]

    response = requests.get(
        f"{BASE_URL}/clients",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_clients_without_auth():
    response = requests.get(
        f"{BASE_URL}/clients"
    )

    assert response.status_code == 401