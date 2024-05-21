# SQLAlchemyを使ってデータベースのテーブルを定義する
# 標準ライブラリ
import os
from typing import List, Optional
# サードパーティライブラリ
from dotenv import load_dotenv
# sqlalchemy内のインポート
from sqlalchemy import create_engine, ForeignKey, String, Integer, Date
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import declarative_base, DeclarativeBase, Mapped, mapped_column, relationship
# .env ファイルをロード
load_dotenv()


# 環境変数からDATABASE_URLを取得する
DATABASE_URL = os.getenv("DATABASE_URL")
# PostgreSQLデータベースに接続するためのengineオブジェクトを作成する
engine = create_engine(DATABASE_URL)

print(f"DATABASE_URL: {DATABASE_URL}")

# ベースクラスを定義する
class Base(DeclarativeBase):
    pass

# テーブルを定義するための基本クラスを定義する
Base = declarative_base() 

# テーブルを表すクラスを定義する。
class Status(Base):
    __tablename__ = "status"
    id=mapped_column(Integer, primary_key=True, autoincrement=True)
    display_name=mapped_column(String,nullable=False)
     
     # ... mapped_column() mappings taskテーブルとのリレーションシップ
    tasks: Mapped[List["Task"]] = relationship("Task",back_populates="status")

class Task(Base):
    __tablename__ = "task"
    id=mapped_column(Integer,primary_key=True,autoincrement=True)
    title=mapped_column(String(30), nullable=False)
    deadline:Mapped[Optional[Date]]=mapped_column(Date, nullable=True)
    status_id=mapped_column(Integer,ForeignKey('status.id'))
   
     # ... mapped_column() mappings Pythonクラス間のリレーションを定義し、オブジェクト間の関連性を扱いやすくする

    status: Mapped["Status"] = relationship("Status",back_populates="task")

# エンジンにベースクラスを関連付ける。 定義されたテーブルをデータベースに作成する
# metadataとは、データベースの様々な情報を保持しているオブジェクト
Base.metadata.create_all(engine)


# テーブルの存在を確認する
inspector = inspect(engine)
tables = inspector.get_table_names()

# テーブル名を出力
print("Tables in the database:", tables)


   
