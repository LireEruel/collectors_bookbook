from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def read_root():
    print("hello world")
    return {"Hello": "Fastapi"}


@app.get("/items/{item_id}/{xyz}")
def read_item(item_id: int, xyz: str, q: Union[str, None] = None):
    return {"item_id": item_id, "xyz": xyz, "q": q}
