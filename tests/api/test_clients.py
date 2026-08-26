import requests


from config import BASE_URL


def test_get_clients(auth_token):
    response = requests.get(
        f"{BASE_URL}/clients",
        headers={
            "Authorization": f"Bearer {auth_token}"
        }
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_client(auth_token):
    

    client_data = {
        "name": "Automation Test Client",
        "phone": "+79990001122",
        "email": "automation@test.com"
    }

    response = requests.post(
        f"{BASE_URL}/clients",
        json=client_data,
        headers={
            "Authorization": f"Bearer {auth_token}"
        }
    )

    assert response.status_code == 200

    client = response.json()

    assert client["name"] == client_data["name"]
    assert client["phone"] == client_data["phone"]
    assert client["email"] == client_data["email"]

def test_get_client_by_id(auth_token):
    

    client_data = {
        "name": "Get Client Test",
        "phone": "+79990001123",
        "email": "getclient@test.com"
    }

    create_response = requests.post(
        f"{BASE_URL}/clients",
        json=client_data,
        headers={
            "Authorization": f"Bearer {auth_token}"
        }
    )

    assert create_response.status_code == 200

    client_id = create_response.json()["id"]

    response = requests.get(
        f"{BASE_URL}/clients/{client_id}",
        headers={
            "Authorization": f"Bearer {auth_token}"
        }
    )

    assert response.status_code == 200
    assert response.json()["id"] == client_id

def test_update_client(auth_token):
    

    client_data = {
        "name": "Update Test Client",
        "phone": "+79990001124",
        "email": "update@test.com"
    }

    create_response = requests.post(
        f"{BASE_URL}/clients",
        json=client_data,
        headers={
            "Authorization": f"Bearer {auth_token}"
        }
    )

    assert create_response.status_code == 200

    client_id = create_response.json()["id"]

    updated_data = {
        "name": "Updated Client",
        "phone": "+79990009999",
        "email": "updated@test.com"
    }

    response = requests.put(
        f"{BASE_URL}/clients/{client_id}",
        json=updated_data,
        headers={
            "Authorization": f"Bearer {auth_token}"
        }
    )

    assert response.status_code == 200

    client = response.json()

    assert client["id"] == client_id
    assert client["name"] == updated_data["name"]
    assert client["phone"] == updated_data["phone"]
    assert client["email"] == updated_data["email"]

def test_delete_client(auth_token):
    

    client_data = {
        "name": "Delete Test Client",
        "phone": "+79990001125",
        "email": "delete@test.com"
    }

    create_response = requests.post(
        f"{BASE_URL}/clients",
        json=client_data,
        headers={
            "Authorization": f"Bearer {auth_token}"
        }
    )

    assert create_response.status_code == 200

    client_id = create_response.json()["id"]

    response = requests.delete(
        f"{BASE_URL}/clients/{client_id}",
        headers={
            "Authorization": f"Bearer {auth_token}"
        }
    )

    assert response.status_code == 200

def test_get_nonexistent_client(auth_token):
    response = requests.get(
        f"{BASE_URL}/clients/999999",
        headers={
            "Authorization": f"Bearer {auth_token}"
        }
    )

    assert response.status_code == 404

def test_delete_nonexistent_client(auth_token):
    response = requests.delete(
        f"{BASE_URL}/clients/999999",
        headers={
            "Authorization": f"Bearer {auth_token}"
        }
    )

    assert response.status_code == 404

def test_create_client_without_name(auth_token):
    client_data = {
        "phone": "+79990001126",
        "email": "noname@test.com"
    }

    response = requests.post(
        f"{BASE_URL}/clients",
        json=client_data,
        headers={
            "Authorization": f"Bearer {auth_token}"
        }
    )

    assert response.status_code == 422

def test_get_clients_with_invalid_token():
    response = requests.get(
        f"{BASE_URL}/clients",
        headers={
            "Authorization": "Bearer invalid_token"
        }
    )

    assert response.status_code == 401

def test_user_cannot_get_another_users_client(
    second_auth_token,
    client_id,
):
    response = requests.get(
        f"{BASE_URL}/clients/{client_id}",
        headers={
            "Authorization": f"Bearer {second_auth_token}"
        },
    )

    assert response.status_code in [403, 404]

def test_user_cannot_update_another_users_client(
    second_auth_token,
    client_id,
):
    updated_data = {
        "name": "Hacked Client",
        "phone": "+79990009999",
        "email": "hacked@test.com",
    }

    response = requests.put(
        f"{BASE_URL}/clients/{client_id}",
        json=updated_data,
        headers={
            "Authorization": f"Bearer {second_auth_token}"
        },
    )

    assert response.status_code in [403, 404]

def test_user_cannot_delete_another_users_client(
    second_auth_token,
    client_id,
):
    response = requests.delete(
        f"{BASE_URL}/clients/{client_id}",
        headers={
            "Authorization": f"Bearer {second_auth_token}"
        },
    )

    assert response.status_code in [403, 404]