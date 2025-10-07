from fastapi.testclient import TestClient
from app.main import app, add

client = TestClient(app)

def test_add_function():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0

def test_health_endpoint():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}

def test_add_endpoint():
    resp = client.get("/add", params={"a": 5, "b": 7})
    assert resp.status_code == 200
    assert resp.json() == {"result": 12}