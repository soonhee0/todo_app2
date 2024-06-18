import pytest
from fastapi.testclient import TestClient
from main import app
from main import app
from settings import Base, Task, Status

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


def test_get_tasks():
    response = client.get("/api/todo/tasks")
    print("test_get_tasks")
    assert response.status_code == 200
    print(response.json())
    assert isinstance(
        response.json(), list
    )  # レスポンスがリスト形式であることを確認する
    tasks = response.json()
    print(tasks)
    assert tasks == [
        {"id": 1, "title": "shopping", "deadline": "2024-06-30", "status_id": 0},
        {
            "id": 2,
            "title": "buy birthday present",
            "deadline": "2024-06-30",
            "status_id": 1,
        },
        {
            "id": 3,
            "title": "finish writing report",
            "deadline": "2024-07-01",
            "status_id": 1,
        },
    ]
