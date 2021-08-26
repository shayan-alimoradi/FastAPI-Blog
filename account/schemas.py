from typing import List, Optional
from pydantic import BaseModel, EmailStr

from blog.schemas import Blog


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: Optional[bool] = True
    blogs: List[Blog] = []

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
