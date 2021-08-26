from sqlalchemy.orm import Session

from fastapi import HTTPException
from pydantic import EmailStr

from . import models, schemas
from .hashing import Hash


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: EmailStr):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = Hash.bcrypt(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(user_id: int, db: Session, user: schemas.UserCreate):
    db_user = db.query(models.User).filter(models.User.id == user_id)
    if not db_user.first():
        raise HTTPException(
            status_code=404, 
            detail=f'User with id {user_id} does not exists'
        )
    db_user.update(user)
    db.commit()
    return 'Done'