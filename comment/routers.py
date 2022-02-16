from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from . import crud, models, schemas
from account.schemas import User
from account.authentication import get_current_active_user
import database

models.database.Base.metadata.create_all(bind=database.engine)

router = APIRouter(prefix="/comments", tags=["comments"])


@router.get("/all/{blog_id}")
async def read_comments(blog_id: int, db: Session = Depends(database.get_db)):
    return await crud.get_all_comments(db, blog_id)


@router.post("/create")
async def create(
    request: schemas.CommentBase,
    db: Session = Depends(database.get_db),
    current_user: User = Depends(get_current_active_user),
):
    return await crud.create_comment(db, request, current_user)
