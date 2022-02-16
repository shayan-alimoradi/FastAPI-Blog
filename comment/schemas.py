from pydantic import BaseModel


class CommentBase(BaseModel):
    content: str
    user_id: int
    blog_id: int
