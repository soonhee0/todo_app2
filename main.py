from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
# from .settings import engine, Base, SessionLocal
from .models import Task,Base
from .database import engine
# FastAPIアプリケーションの作成
app = FastAPI()



# FastAPIのStartupイベントでテーブルを作成する
@app.on_event("startup")
def startup_event():
    # テーブルを作成
    Base.metadata.create_all(bind=engine)

# get_db は、SQLAlchemyのセッションを取得し、使用後に確実にクローズするためのジェネレータ関数
# データベースとの接続を取得する依存関係　関数やクラスが必要とする依存オブジェクトを外部から提供する
def get_db():
    # 新しいデータベースセッションを作成し、変数dbに割り当てる。
    db = SessionLocal()
    try:
        # セッションオブジェクトを呼び出しもとに返す　この時関数の実行は一時停止する
        yield db
    finally:
        # 呼び出し元の処理が終わるとsessionが確実に閉じられる
        db.close()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# # タスク作成エンドポイントの定義
# @app.post("/tasks/")
# async def create_task(title: str, description: str, db: Session = Depends(get_db)):
#     # Taskオブジェクトを作成してセッションに追加
#     db_task = Task(title=title, description=description)
#     db.add(db_task)
#     db.commit()
#     db.refresh(db_task)
#     return db_task

# # タスク一覧取得エンドポイントの定義
# @app.get("/tasks/")
# async def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     tasks = db.query(Task).offset(skip).limit(limit).all()
#     return tasks

# Pythonスクリプトが直接実行された場合
if __name__ == "__main__":
    import uvicorn
    # uvicornを使ってサーバーを起動するためのコード
    # host="0.0.0.0"はサーバーがすべてのネットワークインターフェースで待ち受けることを意味する
    uvicorn.run(app, host="0.0.0.0", port=8000)