from pydantic import BaseModel
from typing import Annotated

class Blog(BaseModel):
    title: Annotated[str, "The title of the blog post"]
    body: Annotated[str, "The content of the blog post"]
