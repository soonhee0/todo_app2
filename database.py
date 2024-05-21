# データベース接続設定と初期化のコード
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os
# .env ファイルをロード
load_dotenv()

## SQLAlchemyのデータベースURLを作成する

# 環境変数からDATABASE_URLを取得する
DATABASE_URL = os.getenv("DATABASE_URL")

# PostgreSQLデータベースに接続するためのengineオブジェクトを作成する
engine = create_engine(DATABASE_URL)

print(f"DATABASE_URL: {DATABASE_URL}")
# テーブルを作成するためのSessionメーカーの作成　Sessionは新しいセッションを作成するためのクラスとなる

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# テーブルを定義するための基本クラスを定義する
Base = declarative_base() 




