# サードパーティライブラリ
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List

# ローカルモジュール
from settings import engine, Base, SessionLocal, Task

app = FastAPI()
# エンジンにベースクラスを関連付ける。 定義されたテーブルをデータベースに作成する
# metadataとは、データベースの様々な情報を保持しているオブジェクト
Base.metadata.create_all(bind=engine)


# get_db は、SQLAlchemyのセッションを取得し、使用後に確実にクローズするためのジェネレータ関数
# データベースとの接続を取得する依存関係　関数やクラスが必要とする依存オブジェクトを外部から提供する
def get_db():
    # 新しいデータベースセッションを作成し、変数dbに割り当てる。
    # このセッションはデータベースへの接続と操作を管理している
    db = SessionLocal()
    try:
        # セッションオブジェクトを呼び出しもと（ged_db関数を呼び出している関数）に返す　この時関数の実行は一時停止する
        yield db
    finally:
        # 呼び出し元の処理が終わるとsessionが確実に閉じられる
        db.close()


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


# セッションを使ってtasksを取得するコードを書く
@app.get("/api/todo/tasks")
# Depends(get_db)を指定することで、パス関数を実行する前にget_dbを実行し、dbインスタンスを取得する 依存性注入


def get_tasks(db: Session = Depends(get_db)):
    #  query()メソッドでデータを選択できる。all()メソッドで全てを選択する

    all_tasks = db.query(Task).all()
    print(all_tasks)
    return all_tasks


# Pythonスクリプトが直接実行された場合
if __name__ == "__main__":
    import uvicorn

    # uvicornを使ってサーバーを起動するためのコード
    # host="0.0.0.0"はサーバーがすべてのネットワークインターフェースで待ち受けることを意味する
    uvicorn.run(app, host="0.0.0.0", port=8000)
