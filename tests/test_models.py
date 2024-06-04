import pytest
import os
from settings import Base, Task, Status, engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv


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
def db_session(postgresql_proc):
    # .envファイルから環境変数を読み込む
    load_dotenv()

    # 環境変数から接続情報を取得
    DATABASE_URL = os.getenv("DATABASE_URL")
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)  # テーブルの作成
    add_dummy_data(session)  # ダミーデータの挿入
    # データベースセッションを一時的に提供する
    # 関数の実行を停止して、add_dummy_data(session) の処理を行う
    # add_dummy_data(session)の処理が終わってから、 db_session()が再開する
    yield session
    session.close()
    Base.metadata.drop_all(engine)  # テーブルの削除


def test_tasks_exist(db_session):
    # Taskテーブルからすべての行を取得してtasksリストに格納する
    tasks = db_session.query(Task).all()
    assert len(tasks) == 3  # ダミーデータの数に基づくアサーション
    # タスクのtitleがダミーデータとして挿入した値と一致するかを確認する
    assert tasks[0].title == "shopping"
    assert tasks[1].title == "buy birthday present"
    assert tasks[2].title == "finish writing report"
