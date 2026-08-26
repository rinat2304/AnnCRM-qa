import allure
import requests

from config import BASE_URL


@allure.feature("Clients")
@allure.story("Get clients")
@allure.title("Получение списка клиентов")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_clients(auth_token):
    with allure.step("Отправить GET-запрос на получение клиентов"):
        response = requests.get(
            f"{BASE_URL}/clients",
            headers={
                "Authorization": f"Bearer {auth_token}"
            }
        )

    with allure.step("Проверить статус ответа 200"):
        assert response.status_code == 200

    with allure.step("Проверить, что ответ содержит список клиентов"):
        assert isinstance(response.json(), list)


@allure.feature("Clients")
@allure.story("Create client")
@allure.title("Создание клиента")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_client(auth_token):
    client_data = {
        "name": "Automation Test Client",
        "phone": "+79990001122",
        "email": "automation@test.com"
    }

    with allure.step("Создать нового клиента"):
        response = requests.post(
            f"{BASE_URL}/clients",
            json=client_data,
            headers={
                "Authorization": f"Bearer {auth_token}"
            }
        )

    with allure.step("Проверить статус ответа 200"):
        assert response.status_code == 200

    client = response.json()

    with allure.step("Проверить данные созданного клиента"):
        assert client["name"] == client_data["name"]
        assert client["phone"] == client_data["phone"]
        assert client["email"] == client_data["email"]


@allure.feature("Clients")
@allure.story("Get client by ID")
@allure.title("Получение клиента по ID")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_client_by_id(auth_token):
    client_data = {
        "name": "Get Client Test",
        "phone": "+79990001123",
        "email": "getclient@test.com"
    }

    with allure.step("Создать тестового клиента"):
        create_response = requests.post(
            f"{BASE_URL}/clients",
            json=client_data,
            headers={
                "Authorization": f"Bearer {auth_token}"
            }
        )

    with allure.step("Проверить успешное создание клиента"):
        assert create_response.status_code == 200

    client_id = create_response.json()["id"]

    with allure.step(f"Получить клиента с ID {client_id}"):
        response = requests.get(
            f"{BASE_URL}/clients/{client_id}",
            headers={
                "Authorization": f"Bearer {auth_token}"
            }
        )

    with allure.step("Проверить статус ответа 200"):
        assert response.status_code == 200

    with allure.step("Проверить ID клиента"):
        assert response.json()["id"] == client_id


@allure.feature("Clients")
@allure.story("Update client")
@allure.title("Обновление клиента")
@allure.severity(allure.severity_level.CRITICAL)
def test_update_client(auth_token):
    client_data = {
        "name": "Update Test Client",
        "phone": "+79990001124",
        "email": "update@test.com"
    }

    with allure.step("Создать тестового клиента"):
        create_response = requests.post(
            f"{BASE_URL}/clients",
            json=client_data,
            headers={
                "Authorization": f"Bearer {auth_token}"
            }
        )

    with allure.step("Проверить успешное создание клиента"):
        assert create_response.status_code == 200

    client_id = create_response.json()["id"]

    updated_data = {
        "name": "Updated Client",
        "phone": "+79990009999",
        "email": "updated@test.com"
    }

    with allure.step(f"Обновить клиента с ID {client_id}"):
        response = requests.put(
            f"{BASE_URL}/clients/{client_id}",
            json=updated_data,
            headers={
                "Authorization": f"Bearer {auth_token}"
            }
        )

    with allure.step("Проверить статус ответа 200"):
        assert response.status_code == 200

    client = response.json()

    with allure.step("Проверить обновленные данные клиента"):
        assert client["id"] == client_id
        assert client["name"] == updated_data["name"]
        assert client["phone"] == updated_data["phone"]
        assert client["email"] == updated_data["email"]


@allure.feature("Clients")
@allure.story("Delete client")
@allure.title("Удаление клиента")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_client(auth_token):
    client_data = {
        "name": "Delete Test Client",
        "phone": "+79990001125",
        "email": "delete@test.com"
    }

    with allure.step("Создать тестового клиента"):
        create_response = requests.post(
            f"{BASE_URL}/clients",
            json=client_data,
            headers={
                "Authorization": f"Bearer {auth_token}"
            }
        )

    with allure.step("Проверить успешное создание клиента"):
        assert create_response.status_code == 200

    client_id = create_response.json()["id"]

    with allure.step(f"Удалить клиента с ID {client_id}"):
        response = requests.delete(
            f"{BASE_URL}/clients/{client_id}",
            headers={
                "Authorization": f"Bearer {auth_token}"
            }
        )

    with allure.step("Проверить статус ответа 200"):
        assert response.status_code == 200


@allure.feature("Clients")
@allure.story("Negative scenarios")
@allure.title("Получение несуществующего клиента")
@allure.severity(allure.severity_level.NORMAL)
def test_get_nonexistent_client(auth_token):
    with allure.step("Запросить несуществующего клиента"):
        response = requests.get(
            f"{BASE_URL}/clients/999999",
            headers={
                "Authorization": f"Bearer {auth_token}"
            }
        )

    with allure.step("Проверить статус ответа 404"):
        assert response.status_code == 404


@allure.feature("Clients")
@allure.story("Negative scenarios")
@allure.title("Удаление несуществующего клиента")
@allure.severity(allure.severity_level.NORMAL)
def test_delete_nonexistent_client(auth_token):
    with allure.step("Попытаться удалить несуществующего клиента"):
        response = requests.delete(
            f"{BASE_URL}/clients/999999",
            headers={
                "Authorization": f"Bearer {auth_token}"
            }
        )

    with allure.step("Проверить статус ответа 404"):
        assert response.status_code == 404


@allure.feature("Clients")
@allure.story("Validation")
@allure.title("Создание клиента без обязательного имени")
@allure.severity(allure.severity_level.NORMAL)
def test_create_client_without_name(auth_token):
    client_data = {
        "phone": "+79990001126",
        "email": "noname@test.com"
    }

    with allure.step("Отправить запрос без обязательного поля name"):
        response = requests.post(
            f"{BASE_URL}/clients",
            json=client_data,
            headers={
                "Authorization": f"Bearer {auth_token}"
            }
        )

    with allure.step("Проверить статус ответа 422"):
        assert response.status_code == 422


@allure.feature("Authorization")
@allure.story("Invalid token")
@allure.title("Получение клиентов с невалидным токеном")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_clients_with_invalid_token():
    with allure.step("Отправить запрос с невалидным токеном"):
        response = requests.get(
            f"{BASE_URL}/clients",
            headers={
                "Authorization": "Bearer invalid_token"
            }
        )

    with allure.step("Проверить статус ответа 401"):
        assert response.status_code == 401


@allure.feature("Authorization")
@allure.story("User isolation")
@allure.title("Пользователь не может получить чужого клиента")
@allure.severity(allure.severity_level.CRITICAL)
def test_user_cannot_get_another_users_client(
    second_auth_token,
    client_id,
):
    with allure.step(f"Попытаться получить чужого клиента с ID {client_id}"):
        response = requests.get(
            f"{BASE_URL}/clients/{client_id}",
            headers={
                "Authorization": f"Bearer {second_auth_token}"
            },
        )

    with allure.step("Проверить запрет доступа"):
        assert response.status_code in [403, 404]


@allure.feature("Authorization")
@allure.story("User isolation")
@allure.title("Пользователь не может изменить чужого клиента")
@allure.severity(allure.severity_level.CRITICAL)
def test_user_cannot_update_another_users_client(
    second_auth_token,
    client_id,
):
    updated_data = {
        "name": "Hacked Client",
        "phone": "+79990009999",
        "email": "hacked@test.com",
    }

    with allure.step(f"Попытаться изменить чужого клиента с ID {client_id}"):
        response = requests.put(
            f"{BASE_URL}/clients/{client_id}",
            json=updated_data,
            headers={
                "Authorization": f"Bearer {second_auth_token}"
            },
        )

    with allure.step("Проверить запрет доступа"):
        assert response.status_code in [403, 404]


@allure.feature("Authorization")
@allure.story("User isolation")
@allure.title("Пользователь не может удалить чужого клиента")
@allure.severity(allure.severity_level.CRITICAL)
def test_user_cannot_delete_another_users_client(
    second_auth_token,
    client_id,
):
    with allure.step(f"Попытаться удалить чужого клиента с ID {client_id}"):
        response = requests.delete(
            f"{BASE_URL}/clients/{client_id}",
            headers={
                "Authorization": f"Bearer {second_auth_token}"
            },
        )

    with allure.step("Проверить запрет доступа"):
        assert response.status_code in [403, 404]