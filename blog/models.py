from sqlmodel import SQLModel, Field
from typing import Annotated, Optional


class Blog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    body: str = Field(index=True)
