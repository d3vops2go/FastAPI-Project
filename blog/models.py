from sqlmodel import SQLModel, Field
from typing import Annotated, Optional


class Blog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: Annotated[str, Field(..., max_length=50, min_length=3)]
    body: Annotated[str, Field(..., max_length=50, min_length=3)]