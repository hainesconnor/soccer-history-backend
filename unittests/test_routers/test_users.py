import json
import random
import string

from fastapi.testclient import TestClient 

from app.main import app

client = TestClient(app)

# TODO implement tests for routes requiring authentication 

def test_create_and_read_users():
    username = "".join(random.choices(string.ascii_lowercase, k=32))
    new_user = {
        "username":username,
        "password":"123"
    }
    response = client.post(
        "/users/",
        json=new_user
    )

    assert response.status_code == 200
    body = response.json()
    assert body["username"] == username
 
    
    # response = client.get("/users")
    # assert response.status_code == 200
    # body = response.json()
    # print(body)



# TODO implement tests for crud.py
