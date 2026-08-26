import os


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