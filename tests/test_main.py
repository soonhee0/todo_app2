from fastapi import FastAPI
from fastapi.testclient import TestClient


from todo_app2.main import app

client = TestClient(app)


def test_read_tasks_empty():
    response = client.get("/todo/tasks")
    assert response.status_code == 200
    assert response.json() == []
