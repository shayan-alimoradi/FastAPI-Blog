from fastapi import HTTPException
from sqlalchemy.orm import Session

from . import models, schemas
from account.schemas import Blog


async def get_blog(db: Session, blog_id: int):
    return db.query(models.Blog).filter(models.Blog.id == blog_id).first()


async def get_blog_by_title(db: Session, title: str):
    return db.query(models.Blog).filter(models.Blog.title == title).first()


async def get_blogs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Blog).offset(skip).limit(limit).all()


async def create_blog(db: Session, blog: schemas.BlogCreate):
    db_blog = models.Blog(
        title=blog.title,
        description=blog.description,
        available=blog.available,
        user_id=blog.user_id,
    )
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog


async def update_Blog(blog_id: int, request: schemas.BlogBase, db: Session):
    db_blog = db.query(models.Blog).filter(models.Blog.id == blog_id)
    if not db_blog.first():
        raise HTTPException(
            status_code=404, detail=f"Blog with id {blog_id} does not exists"
        )

    db_blog.update(
        {
            models.Blog.title: request.title,
            models.Blog.description: request.description,
            models.Blog.available: request.available,
        }
    )
    db.commit()
    return "Updated Successfully"


async def delete_blog(blog_id: int, db: Session):
    db.query(models.Blog).filter(models.Blog.id == blog_id).delete(
        synchronize_session=False
    )
    db.commit()
    return "Deleted Successfully"
