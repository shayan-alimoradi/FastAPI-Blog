from fastapi import Depends
from sqlalchemy.orm import Session

from datetime import datetime

from . import models, schemas
from account.authentication import get_current_active_user
from account.schemas import User


async def create_comment(
    db: Session,
    request: schemas.CommentBase,
    current_user: User = Depends(get_current_active_user),
):
    new_comment = models.Comment(
        user_id=current_user.id,
        content=request.content,
        blog_id=request.blog_id,
        time_stamp=datetime.now(),
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


async def get_all_comments(db: Session, blog_id: int):
    return db.query(models.Comment).filter(models.Comment.id == blog_id).all()
