def test_user_registration(client):
    payload = {
        "name": "Test User",
        "email": "test_user_1@example.com",
        "password": "password123"
    }

    response = client.post("/auth/register", json=payload)

    data = response.json()

    assert response.status_code == 200