from fastapi import FastAPI

app = FastAPI()


# https://qiita.com/XPT60/items/deac8d6155da58afbb6f


@app.get("/")
def index():
    return {"msg": "Hello World"}


@app.get("/users/{user_id}")
def read_item(user_id: int):
    return {"user_id": user_id}
