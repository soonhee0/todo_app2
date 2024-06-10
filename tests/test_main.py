# FastAPIを使用してウェブAPIエンドポイントをテストする
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pathlib import Path
import sys


# importしたい親の親のパッケージをモジュール検索に追加する
sys.path.append(str(Path(__file__).resolve().parent.parent))
from main import app

client = TestClient(app)


# dbにダミーデータを登録したので、test_read_tasks_empty()テストはコメントアウトする
# def test_read_tasks_empty():
#     response = client.get("/api/todo/tasks")

#     # レスポンスが200 OKであることを確認
#     assert response.status_code == 200

#     try:
#         # レスポンスの内容がJSONであることを確認
#         response_json = response.json()
#         assert response_json == []
#     except:
#         # 例外が発生した場合、テストを失敗させる
#         assert False, "An unexpected exception"
