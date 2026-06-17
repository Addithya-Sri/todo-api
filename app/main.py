from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid

app = FastAPI(title="Todo API", version="1.0.0")

# In-memory storage (acts as our database for now)
todos = {}


class TodoCreate(BaseModel):
    task: str


class Todo(BaseModel):
    id: str
    task: str
    completed: bool = False


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/todos")
def get_todos():
    return list(todos.values())


@app.post("/todos", status_code=201)
def create_todo(payload: TodoCreate):
    todo_id = str(uuid.uuid4())
    todo = Todo(id=todo_id, task=payload.task)
    todos[todo_id] = todo.model_dump()
    return todo


@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: str):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    del todos[todo_id]
