from typing import Optional
from pydantic import BaseModel


class BlogBase(BaseModel):
    title: str
    description: Optional[str] = None
    available: Optional[bool] = True


class BlogCreate(BlogBase):
    pass


class Blog(BlogBase):
    class Config:
        orm_mode = True
