from contextlib import asynccontextmanager
from typing import Annotated, Optional
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.params import Query
from sqlmodel import Session, select
from blog import schemas, models
from blog.database import create_db_and_tables, get_session


SessionLocal = Depends(get_session)


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

###########################
### BLOG CRUD OPS  ########
###########################


@app.post("/blog", status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = SessionLocal):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/blog", status_code=status.HTTP_200_OK)
def get_blogs(
    limit: Optional[int] = None, db: Session = SessionLocal
) -> list[models.Blog]:
    if limit != None and limit <= 0:
        raise HTTPException(
            status_code=400,
            detail="Limit must be a positive integer and greater than Zero",
        )
    blog_list = db.exec(select(models.Blog).limit(limit)).all()
    return blog_list


@app.get('/blog/{blog_id}', status_code= status.HTTP_200_OK)
def get_blog_by_id(blog_id: int, db: Session = SessionLocal) -> models.Blog:
    blog = db.get(models.Blog, blog_id)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {blog_id} not found"
        )
    return blog


@app.delete('/blog/{blog_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(blog_id: int, db: Session = SessionLocal):
    blog = db.get(models.Blog, blog_id)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {blog_id} not found"
        )
    db.delete(blog)
    db.commit()
    return 'Successfully deleted'
