from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] = True


@app.get("/blog")
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"data": f"{limit} published blogs from db"}
    else:
        return {"data": f"{limit} blogs from db"}


@app.post("/blog")
def create_blog(blog: Blog):
    return {"message" : f"{blog.title} is created"}


@app.get("/blog/unpublished")
async def unpublished():
    return {"data": "all unpublished blogs"}


@app.get("/blog/{id}")
def show(id: int):
    return {"data": f"blog with id {id}"}


@app.get("/blog/{id}/comments")
def comments(id: int, limit: Optional[int]):
    return {"data": f"all comments for blog with id {id}"}


# if __name__ == '__main__':
# uvicorn.run(app, port=8080, host='0.0.0.0')
