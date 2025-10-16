import os
import random
import string
import allure
import pytest

from common.config_loader import load_config
from common.http_client import HttpClient
from api.users import UsersAPI

def _rand_str(n=6):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=n))

@pytest.fixture(scope="session")
def settings():
    return load_config()

@pytest.fixture(scope="session")
def api_client(settings):
    token = settings.get("auth", {}).get("token") or None
    return HttpClient(
        base_url=settings["base_url"],
        timeout=settings.get("request", {}).get("timeout", 10),
        retries=settings.get("request", {}).get("retries", 2),
        token=token,
    )

@pytest.fixture(scope="session")
def users_api(api_client):
    return UsersAPI(api_client)

@pytest.fixture
def random_user_payload():
    uname = f"u_{_rand_str(8)}"
    return {
        "username": uname,
        "email": f"{uname}@example.com",
        "password": "Passw0rd!"
    }

@pytest.fixture
def ensure_cleanup(users_api):
    created_ids = []

    yield type("Cleanup", (), {
        "add_user": lambda self, uid: created_ids.append(uid)
    })()

    for uid in created_ids:
        with allure.step(f"Cleanup: delete user {uid}"):
            users_api.delete_user(uid)
