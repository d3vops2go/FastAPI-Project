from sqlmodel import SQLModel, SQLModel, create_engine, Session
from blog.models import Blog

DATBASE_URL = "sqlite:///./blog.db"
connect_args = {"check_same_thread": False}
engine = create_engine(DATBASE_URL, connect_args=connect_args)

def get_session():
    with Session(engine) as session:
        yield session

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)