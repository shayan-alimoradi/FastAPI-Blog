from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from account.authentication import get_current_active_user
from account.schemas import User, Blog

import database

models.database.Base.metadata.create_all(bind=database.engine)

router = APIRouter(prefix="/blogs", tags=["blogs"])


@router.get("/", response_model=List[Blog])
async def read_blogs(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(database.get_db),
    current_user: User = Depends(get_current_active_user),
):
    blogs = await crud.get_blogs(db, skip=skip, limit=limit)
    return blogs


@router.get("/{blog_id}", response_model=Blog)
async def read_blog(blog_id: int, db: Session = Depends(database.get_db)):
    db_blog = await crud.get_blog(db=db, blog_id=blog_id)
    if db_blog is None:
        raise HTTPException(
            status_code=404, detail=f"Blog with id {blog_id} does not exists"
        )
    return db_blog


@router.post("/create", response_model=Blog, status_code=201)
async def create_blog(
    blog: schemas.BlogCreate,
    db: Session = Depends(database.get_db),
    current_user: User = Depends(get_current_active_user),
):
    db_blog = await crud.get_blog_by_title(db, title=blog.title)
    if db_blog:
        raise HTTPException(
            status_code=400, detail=f"Blog with title {blog.title} already exists"
        )
    return await crud.create_blog(db=db, blog=blog)


@router.delete("/destroy/{blog_id}", status_code=204)
async def delete_blog(
    blog_id: int,
    db: Session = Depends(database.get_db),
    current_user: User = Depends(get_current_active_user),
):
    await crud.delete_blog(blog_id, db)


@router.put("/update/{blog_id}", status_code=200)
async def update_blog(
    blog_id: int,
    request: Blog,
    db: Session = Depends(database.get_db),
    current_user: User = Depends(get_current_active_user),
):
    return await crud.update_Blog(blog_id, request, db)
