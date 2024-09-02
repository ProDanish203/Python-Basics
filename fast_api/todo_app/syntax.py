from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class TodoItem(BaseModel):
    title: str
    description: str | None = None
    completed: bool | None = None


@app.get("/")
def root():
    return {"message": "Hello World from FastAPI"}


# Params
@app.get("/todos/{id}")
def getById(id):
    return {"message": f"Get todo by id {id}"}


# Query Params
@app.get("/todos")
def getItemByQueryParams(filter="atoz", page=1):
    return {"message": f"Get item by filter {filter} and page {page}"}


# Post Request
@app.post("/todos")
def createItem(item: TodoItem):
    return {"message": f"Create item {item}"}
