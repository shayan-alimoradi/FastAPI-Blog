from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from datetime import timedelta

from . import schemas, models
from .token import create_access_token
from .hashing import Hash
import database


router = APIRouter(tags=["authentication"])


@router.post("/sign-in")
def sign_in(
    request: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(database.get_db),
):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="Invalid Credentials")

    if not Hash.verify(user.hashed_password, request.password):
        raise HTTPException(status_code=400, detail="Invalid Email or Password")
    # generate the jwt token
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
