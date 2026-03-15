import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture
def client():
    """
    Basic TestClient fixture used for unauthenticated requests.
    """
    with TestClient(app) as client:
        yield client


@pytest.fixture
def test_user(client):

    payload = {
        "name": "Pytest User",
        "email": "pytest@example.com",
        "password": "password123"
    }

    response = client.post("/auth/register", json=payload)
    return response.json()


@pytest.fixture
def token(client, test_user):

    payload = {
        "username": "pytest@example.com",
        "password": "password123"
    }

    response = client.post("/auth/login", data=payload)

    return response.json()["access_token"]


@pytest.fixture
def authorized_client(client, token):
    """
    Returns a client with Authorization header attached.
    """
    client.headers = {
        "Authorization": f"Bearer {token}"
    }

    return client