from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from blog.schemas import Blog
from blog.database import create_db_and_tables, get_session

SessionLocal = Depends(get_session)

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)



@app.post("/blog")
def create_blog(blog: Blog):
    return blog