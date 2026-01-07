from pydantic import BaseModel, Field
from typing import Annotated


class Blog(BaseModel):
    title: Annotated[str, Field(..., max_length=50, min_length=3)]
    body: Annotated[str, Field(..., max_length=50, min_length=3)]
