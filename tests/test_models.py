import pytest
import os
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
from settings import Base, Task, Status


# ダミーデータを挿入する関数
def add_dummy_data(session):

    # Status データの挿入
    status = [
        Status(id="0", display_name="pending"),
        Status(id="1", display_name="completed"),
    ]

    # status リストに含まれるすべてのオブジェクトを現在のデータベースセッションに追加
    session.add_all(status)

    # セッション内のすべての変更をデータベースに保存する
    session.commit()

    tasks = [
        Task(id="1", title="shopping", deadline="2024-06-30", status_id="0"),
        Task(
            id="2", title="buy birthday present", deadline="2024-06-30", status_id="1"
        ),
        Task(
            id="3", title="finish writing report", deadline="2022-07-01", status_id="1"
        ),
    ]
    session.add_all(tasks)
    session.commit()


# pytest フィクスチャ
# db_sessionはテスト用のデータベースセッションをセットアップするフィクスチャ
@pytest.fixture(scope="module")
def db_session():
    # テスト用データベースURLを環境変数から取得
    load_dotenv()
    TEST_SQLALCHEMY_DATABASE_URL = os.getenv("TEST_SQLALCHEMY_DATABASE_URL")

    # そのデータベースURLを使用してデータベースエンジンを作成
    engine = create_engine(TEST_SQLALCHEMY_DATABASE_URL)

    # データベースを作成する
    Session = sessionmaker(bind=engine)

    # セッションのcommitメソッドをオーバーライド（親クラスからcommitメソッドを継承する）
    class TestSession(Session):
        def commit(self):
            pass  # 実際には何も行わない

    session = TestSession()

    # テーブルを自動で作成する
    Base.metadata.create_all(engine)

    add_dummy_data(session)  # ダミーデータの挿入

    # データベースセッションを一時的に提供する
    # 関数の実行を停止して、add_dummy_data(session) の処理を行う
    # add_dummy_data(session)の処理が終わってから、 db_session()が再開する
    yield session  # セッションを開始する
    session.close()
    Base.metadata.drop_all(engine)  # テーブルの削除


def test_db_connection(db_session):
    try:
        inspector = inspect(db_session.bind)
        tables = inspector.get_table_names()
        print(f"Tables in the database: {tables}")
        assert len(tables) > 0
        print("Database connection is verified.")
    except Exception as e:
        pytest.fail(f"Database connection failed: {e}")
