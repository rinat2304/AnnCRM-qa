import allure
import requests

import os

BASE_URL = os.getenv(
    "BASE_URL",
    "http://127.0.0.1:8000"
)


@allure.feature("Authentication")
@allure.story("Login")
@allure.title("Успешная авторизация пользователя")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_success():

    with allure.step("Отправить запрос на авторизацию"):
        response = requests.post(
            f"{BASE_URL}/auth/login",
            data={
                "username": "qaz@qaz.qaz",
                "password": "qazqaz",
            },
        )

    with allure.step("Проверить статус ответа 200"):
        assert response.status_code == 200

    with allure.step("Проверить наличие access token"):
        assert "access_token" in response.json()


@allure.feature("Authentication")
@allure.story("Login")
@allure.title("Авторизация с неверным паролем")
@allure.severity(allure.severity_level.NORMAL)
def test_login_invalid_password():

    with allure.step("Отправить запрос с неверным паролем"):
        response = requests.post(
            f"{BASE_URL}/auth/login",
            data={
                "username": "qaz@qaz.qaz",
                "password": "wrong_password",
            },
        )

    with allure.step("Проверить статус ответа 401"):
        assert response.status_code == 401


@allure.feature("Authorization")
@allure.story("Access clients with authentication")
@allure.title("Авторизованный пользователь получает список клиентов")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_clients_with_auth():

    with allure.step("Авторизоваться"):
        login_response = requests.post(
            f"{BASE_URL}/auth/login",
            data={
                "username": "qaz@qaz.qaz",
                "password": "qazqaz",
            },
        )

    with allure.step("Проверить успешную авторизацию"):
        assert login_response.status_code == 200

    token = login_response.json()["access_token"]

    with allure.step("Получить список клиентов"):
        response = requests.get(
            f"{BASE_URL}/clients",
            headers={
                "Authorization": f"Bearer {token}"
            },
        )

    with allure.step("Проверить статус ответа 200"):
        assert response.status_code == 200

    with allure.step("Проверить, что ответ содержит список"):
        assert isinstance(response.json(), list)


@allure.feature("Authorization")
@allure.story("Access clients without authentication")
@allure.title("Неавторизованный пользователь не получает список клиентов")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_clients_without_auth():

    with allure.step("Отправить запрос без Authorization"):
        response = requests.get(
            f"{BASE_URL}/clients"
        )

    with allure.step("Проверить статус ответа 401"):
        assert response.status_code == 401