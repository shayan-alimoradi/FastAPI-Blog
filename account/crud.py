from sqlalchemy.orm import Session

from fastapi import HTTPException
from pydantic import EmailStr

from . import models, schemas
from .hashing import Hash


async def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


async def get_user_by_username(db: Session, username: EmailStr):
    return db.query(models.User).filter(models.User.username == username).first()


async def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


async def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = Hash.bcrypt(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


async def update_user(user_id: int, db: Session, user: schemas.UserCreate):
    db_user = db.query(models.User).filter(models.User.id == user_id)
    if not db_user.first():
        raise HTTPException(
            status_code=404, detail=f"User with id {user_id} does not exists"
        )
    db_user.update(
        {
            models.User.email: user.email,
            models.User.hashed_password: Hash.bcrypt(user.password),
        }
    )
    db.commit()
    return "Done"


async def delete_user(user_id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    db.delete(user)
    db.commit()
    return "Done"
