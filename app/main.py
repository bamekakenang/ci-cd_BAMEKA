from fastapi import FastAPI
<<<<<<< HEAD

app = FastAPI()

def add(a: int, b: int) -> int:
    return a + b

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/add")
def add_route(a: int, b: int):
    return {"result": add(a, b)}
=======
from pydantic import BaseModel

app = FastAPI(title="CI/CD Demo API", version="1.0.0")

class AddRequest(BaseModel):
    a: float
    b: float

def add(a: float, b: float) -> float:
    """Additionne deux nombres."""
    return a + b

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/add")
def add_query(a: float, b: float):
    return {"result": add(a, b)}

@app.post("/add")
def add_body(payload: AddRequest):
    return {"result": add(payload.a, payload.b)}
>>>>>>> 19c9cfa (Init CI/CD: app FastAPI, tests, Docker, workflows)
