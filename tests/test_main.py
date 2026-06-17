from fastapi.testclient import TestClient
from app.main import app, todos

client = TestClient(app)


def setup_function():
    todos.clear()


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_todo():
    response = client.post("/todos", json={"task": "Learn CI/CD"})
    assert response.status_code == 201
    assert response.json()["task"] == "Learn CI/CD"


def test_delete_todo():
    create_response = client.post("/todos", json={"task": "Learn Docker"})
    todo_id = create_response.json()["id"]
    delete_response = client.delete(f"/todos/{todo_id}")
    assert delete_response.status_code == 204
