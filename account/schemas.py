from typing import List, Optional
from pydantic import BaseModel, EmailStr

from blog.schemas import BlogBase


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: Optional[bool] = True
    blogs: List[BlogBase] = []

    class Config:
        orm_mode = True


# User for Blog
class UserBlog(UserBase):
    id: int
    is_active: Optional[bool] = True

    class Config:
        orm_mode = True


class Blog(BlogBase):
    id: int
    user: UserBlog = None

    class Config:
        orm_mode = True


class SignIn(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[EmailStr] = None
