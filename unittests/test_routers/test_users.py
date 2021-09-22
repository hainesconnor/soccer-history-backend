import random
import string

from fastapi.testclient import TestClient

from unittests.utils import random_username

from app.main import app

client = TestClient(app)

# TODO refactor database to include "super users", so these tests can be decoupled
# Currently I'm creating a user, and then using that created user for the additional tests


def test_create_and_read_users():

    # Test Create User
    username = random_username()
    new_user = {
        "username": username,
        "password": "123"
    }
    response = client.post(
        "/users/",
        json=new_user
    )

    assert response.status_code == 200
    user = response.json()
    assert user["username"] == username

    # Test Get Users
    response = client.get("/users")
    assert response.status_code == 200
    users = response.json()
    assert user in users

    # Test Get User by Id
    user_id = user["id"]
    response = client.get(f'/users/{user_id}')
    assert response.status_code == 200
    user = response.json()
    assert user["username"] == username

    # Negative test - Create User
    user = {"test": "hi"}
    response = client.post("/users/", json=user)
    assert response.status_code == 422

    # Negative test - Get Users by Id
    response = client.get("/users/12222.22")
    assert response.status_code == 422


def test_read_user_me():
    response = client.get("/users/me")
    assert response.status_code == 401

    # TODO implement happy path tests for routes requiring authentication


def test_post_token():
    response = client.post("/token")
    assert response.status_code == 422

    # TODO implement happy path test and test for incorrect username or password
