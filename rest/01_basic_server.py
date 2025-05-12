import fastapi

app = fastapi.FastAPI()


@app.get("/hello")
def hello():
    result = 2 + 2
    return {"hello": "world", "result": result}


@app.get("/hello_with_query")
def hello_with_query(name: str):
    return {"hello": name}


def super_profitable_model(year_born: int) -> int:
    return 2025 - year_born


@app.get("/model")
def model(year_born: int):
    result = super_profitable_model(year_born)
    is_old = (result > 26)

    return {"age": result, "is_old": is_old}
