from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session

from account.schemas import User

from . import models, schemas
from account.authentication import get_current_active_user


async def get_blog(db: Session, blog_id: int):
    return db.query(models.Blog).filter(models.Blog.id == blog_id).first()


async def get_blog_by_title(db: Session, title: str):
    return db.query(models.Blog).filter(models.Blog.title == title).first()


async def get_blogs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Blog).offset(skip).limit(limit).all()


async def create_blog(
    db: Session,
    blog: schemas.BlogCreate,
    current_user: User = Depends(get_current_active_user),
):
    db_blog = models.Blog(
        title=blog.title,
        description=blog.description,
        available=blog.available,
        user_id=current_user.id,
    )
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog


async def update_Blog(blog_id: int, request: schemas.BlogBase, db: Session, current_user: User = Depends(get_current_active_user)):
    db_blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not db_blog:
        raise HTTPException(
            status_code=404, detail=f"Blog with id {blog_id} does not exists"
        )
    
    if db_blog.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="You're not the owner of this blog")

    db_blog.update(
        {
            models.Blog.title: request.title,
            models.Blog.description: request.description,
            models.Blog.available: request.available,
        }
    )
    db.commit()
    return "Updated Successfully"


async def delete_blog(
    blog_id: int, db: Session, current_user: User = Depends(get_current_active_user)
):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=404, detail=f"Post with id {blog_id} not found")
    if blog.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="You're not the owner of this blog")
    db.delete(blog)
    db.commit()
    return "Deleted Successfully"
