import pytest
from sqlalchemy import inspect


def test_db_connection(db_session):
    try:
        # データベースエンジンからインスペクターを作成する。インスペクターによってテーブルの要素を取得したりできる
        inspector = inspect(db_session.bind)
        tables = inspector.get_table_names()
        print(f"Tables in the database: {tables}")
        assert len(tables) > 0
        print("Database connection is verified.")
    except Exception as e:
        pytest.fail(f"Database connection failed: {e}")
