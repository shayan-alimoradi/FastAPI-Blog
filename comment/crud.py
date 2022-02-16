from sqlalchemy.orm import Session

from datetime import datetime

from . import models, schemas


async def create_comment(db: Session, request: schemas.CommentBase):
    new_comment = models.Comment(
        user_id=request.user_id,
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
