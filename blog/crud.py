from sqlalchemy.orm import Session

from . import models, schemas


def get_blog(db: Session, blog_id: int):
    return db.query(models.Blog).filter(
        models.Blog.id == blog_id
    ).first()


def get_blog_by_title(db: Session, title: str):
    return db.query(models.Blog).filter(
        models.Blog.title == title
    ).first()


def get_blogs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Blog).offset(skip).limit(limit).all()


def create_blog(db: Session, blog: schemas.BlogCreate):
    db_blog = models.Blog(
        owner_id=1,
        title=blog.title,
        description=blog.description,
        available=blog.available
    )
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog


def update_Blog(db: Session, blog: schemas.BlogCreate, blog_id: int):
    db_blog = db.query(models.Blog).filter(
        models.Blog.title == blog_id
    )
    db_blog.update(blog)
    db.commit()
    db.refresh(db_blog)
    return 'Updated Successfully'