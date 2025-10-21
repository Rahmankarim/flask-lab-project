import json
import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert b"OK" in response.data

def test_post_data_json(client):
    payload = {"name": "Rahman", "task": "lab"}
    response = client.post("/data", json=payload)
    assert response.status_code == 201
    data = response.get_json()
    assert data["status"] == "received"
    assert data["data"] == payload

def test_post_data_empty(client):
    response = client.post("/data", data={})
    # No data -> 400 as defined in app
    assert response.status_code == 400
