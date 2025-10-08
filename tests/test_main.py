<<<<<<< HEAD
=======
import math
>>>>>>> 19c9cfa (Init CI/CD: app FastAPI, tests, Docker, workflows)
from fastapi.testclient import TestClient
from app.main import app, add

client = TestClient(app)

<<<<<<< HEAD
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
=======
def test_add_function_basic():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert math.isclose(add(1.5, 2.5), 4.0)

def test_root_ok():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_add_query():
    r = client.get("/add", params={"a": 2, "b": 3})
    assert r.status_code == 200
    assert r.json()["result"] == 5

def test_add_body():
    r = client.post("/add", json={"a": 2.5, "b": 0.5})
    assert r.status_code == 200
    assert r.json()["result"] == 3.0
>>>>>>> 19c9cfa (Init CI/CD: app FastAPI, tests, Docker, workflows)
