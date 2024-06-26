# サードパーティライブラリ
from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from sqlalchemy.exc import OperationalError
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
    # インスタンス化
    db = SessionLocal()
    try:
        # セッションオブジェクトを呼び出しもと（ged_db関数を呼び出している関数）に返す　この時関数の実行は一時停止する
        yield db
    except OperationalError:
        raise HTTPException(status_code=500, detail="Could not connect to the database")
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


# 特定のタスク取得
@app.get("/api/todo/tasks/{task_id}")
# get_db 関数を呼び出し、その戻り値を db パラメータに設定する
def get_task(task_id: int, db: Session = Depends(get_db)):
    if task_id < 0:
        raise HTTPException(
            status_code=400, detail="Task ID must be a non-negative integer"
        )
    # Task.idはTaskテーブルのidカラムでtask_idはパスパラメータとして渡されたid
    # first()でフィルタリングされた中で最初の値を指す
    particular_task = db.query(Task).filter(Task.id == task_id).first()

    if particular_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return particular_task


# タスクの作成
@app.post("/api/todo/tasks")
# 受け取ったリクエストデータをpydanticモデルのTaskモデルに割り当てられ、task変数に変換
# これにより、Taskモデルに従って、関数内でtask変数が扱えるようになる
def create_task(task: Task, db: Session = Depends(get_db)):

    db.add(task)
    db.commit()
    # 最新のデータベースの内容をtask変数に反映する
    db.refresh(task)
    print(task)
    return task


@app.exception_handler(StarletteHTTPException)
# request オブジェクトは現在のHTTPリクエストを表す
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return JSONResponse(status_code=404, content={"detail": "Task not found"})
    elif exc.status_code == 400:

        return JSONResponse(
            status_code=400,
            content={"detail": "Task ID must be a non-negative integer"},
        )
    else:
        return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})


@app.exception_handler(OperationalError)
async def operational_error_handler(request, exc: OperationalError):
    return JSONResponse(
        status_code=500, content={"detail": "Could not connect to the database"}
    )


# Pythonスクリプトが直接実行された場合
if __name__ == "__main__":
    import uvicorn

    # uvicornを使ってサーバーを起動するためのコード
    # host="0.0.0.0"はサーバーがすべてのネットワークインターフェースで待ち受けることを意味する
    uvicorn.run(app, host="0.0.0.0", port=8000)
