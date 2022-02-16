from pydantic import BaseModel


class CommentBase(BaseModel):
    username: str
    content: str
    post_id: int
