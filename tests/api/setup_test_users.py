import requests

from config import (
    BASE_URL,
    TEST_EMAIL,
    TEST_PASSWORD,
    SECOND_TEST_EMAIL,
    SECOND_TEST_PASSWORD,
)


def create_user(username, email, password):
    response = requests.post(
        f"{BASE_URL}/auth/register",
        json={
            "username": username,
            "email": email,
            "password": password,
        },
    )

    if response.status_code in [200, 201]:
        print(f"Created test user: {email}")
        return

    if response.status_code == 400:
        print(
            f"User may already exist: {email}. "
            f"Response: {response.text}"
        )
        return

    raise RuntimeError(
        f"Failed to create test user {email}: "
        f"{response.status_code} {response.text}"
    )


if __name__ == "__main__":
    create_user(
        "qa_user_1",
        TEST_EMAIL,
        TEST_PASSWORD,
    )

    create_user(
        "qa_user_2",
        SECOND_TEST_EMAIL,
        SECOND_TEST_PASSWORD,
    )

    print("Test users are ready")