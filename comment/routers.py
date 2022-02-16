from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from . import crud, models, schemas
from account.schemas import UserAuth
from account.OAuth2 import get_current_user
import database

models.database.Base.metadata.create_all(bind=database.engine)

router = APIRouter(prefix="/comments", tags=["comments"])


@router.get('/all/{post_id}')
async def read_comments(post_id: int, db: Session = Depends(database.get_db)):
    return crud.get_all_comments(db, post_id)


@router.post('/create')
async def create(
    request: schemas.CommentBase, 
    db: Session = Depends(database.get_db),
    current_user: UserAuth = Depends(get_current_user)
):
    return crud.create_comment(db, request)
