# 　環境変数のロードをするファイル
from sqlalchemy import create_engine
# from typing import List,Optional

# from sqlalchemy.orm import declarative_base
# from sqlalchemy.orm import sessionmaker
from sqlalchemy.inspection import inspect
# from dotenv import load_dotenv
from .database import engine, Base
import os


# エンジンにベースクラスを関連付ける。 定義されたテーブルをデータベースに作成する
# metadataとは、データベースの様々な情報を保持しているオブジェクト
Base.metadata.create_all(engine)



# テーブルの存在を確認する
inspector = inspect(engine)
tables = inspector.get_table_names()

# テーブル名を出力
print("Tables in the database:", tables)


   
