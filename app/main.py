from fastapi import FastAPI

app = FastAPI()

def add(a: int, b: int) -> int:
    return a + b

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/add")
def add_route(a: int, b: int):
    return {"result": add(a, b)}