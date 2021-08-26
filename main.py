from fastapi import FastAPI

from account.routers import router as users_router
from account.authentication import router as authentication_router
from blog.routers import router as blog_router

app = FastAPI()


app.include_router(users_router)
app.include_router(authentication_router)
app.include_router(blog_router)
