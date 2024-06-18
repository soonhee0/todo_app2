# FastAPIを使用してウェブAPIエンドポイントをテストする
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pathlib import Path
import sys
from settings import SessionLocal
from sqlalchemy.exc import OperationalError
from main import app, SessionLocal, get_db
from unittest.mock import Mock, patch

# 指定された対象をモックに置き換えるための関数
from unittest.mock import patch

# PythonオブジェクトをJSON互換の形式に変換するために使用される
from fastapi.encoders import jsonable_encoder

# importしたい親の親のパッケージをモジュール検索に追加する
sys.path.append(str(Path(__file__).resolve().parent.parent))
from main import app

client = TestClient(app)


# 正常系のテスト
def test_read_tasks_with_data(db_session):
    response = client.get("/api/todo/tasks")

    # レスポンスが200 OKであることを確認
    assert response.status_code == 200

    try:
        # APIから出力した値をJSONに変換して変数response_jsonに格納する
        response_json = response.json()

        expected_tasks = [
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
        assert response_json == expected_tasks
    except:
        # 例外が発生した場合、テストを失敗させる
        assert False, "An unexpected exception"


# 異常系のテスト
# 不正なパラメータ
# task_idが負の値の場合にエラーを発生させる
def test_read_tasks_with_invalid_id():
    response = client.get("/api/todo/tasks/-1")
    assert response.status_code == 400
    assert response.json() == {"detail": "Task ID must be a non-negative integer"}


def test_get_task_nonexistent_id():
    response = client.get("/api/todo/tasks/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}

    # SessionLocalのコンストラクタがOperationalErrorを投げるようにモックする


# DBサーバーが応答不可　接続を失敗した場合のエラーハンドリングをテスト
def test_db_connection_failure(monkeypatch):

    def mock_session():
        # OperationalErrorの引数（エラーメッセージ、エラーコード、追加情報）
        raise OperationalError("mock", "mock", "mock")

    # get_dbで例外を発生させる
    app.dependency_overrides[get_db] = mock_session

    # SessionLocalが呼び出されるたびにmock_sessionが実行される
    monkeypatch.setattr("settings.SessionLocal", mock_session)
    # データベース接続の失敗をシミュレーションする
    response = client.get("/api/todo/tasks")

    assert response.status_code == 500
    assert response.json() == {"detail": "Could not connect to the database"}
