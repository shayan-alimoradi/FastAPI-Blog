from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship

import database


class Comment(database.Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    content = Column(String)
    time_stamp = Column(DateTime)
    post_id = Column(Integer, ForeignKey('posts.id'))

    post_cm = relationship('Post', back_populates='comments')
