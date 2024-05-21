from sqlalchemy import ForeignKey, String, Integer, Date, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


# ベースクラスを定義する
class Base(DeclarativeBase):
    pass
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