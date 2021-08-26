from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
import database

models.database.Base.metadata.create_all(bind=database.engine)

router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.get('/{user_id}', response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(database.get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=404, 
            detail=f'User with id {user_id} does not exists'
        )
    return db_user


@router.get('/', response_model=List[schemas.User])
def read_users(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(database.get_db)
):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.post('/create', response_model=schemas.User, status_code=201)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail='Email already registered')
    return crud.create_user(db=db, user=user)