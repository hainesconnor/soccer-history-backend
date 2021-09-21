import json

from fastapi.testclient import TestClient 

from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/matches")
    assert response.status_code == 200
    body = response.json()
    assert len(body) == 100



# TODO implement tests for crud.py
