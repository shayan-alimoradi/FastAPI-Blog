from sqlalchemy.orm import Session

from datetime import datetime

from . import models, schemas


def create_comment(db: Session, request: schemas.CommentBase):
    new_comment = models.Comment(
        username=request.username,
        content=request.content,
        post_id=request.post_id,
        time_stamp=datetime.now()
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


def get_all_comments(db: Session, post_id: int):
    return db.query(models.Comment).filter(models.Comment.id == post_id).all()
