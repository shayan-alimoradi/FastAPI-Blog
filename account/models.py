from sqlalchemy import (
    Column,
    String,
    Integer,
    Boolean,
)
from sqlalchemy.orm import relationship

import database


class User(database.Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    blogs = relationship("Blog", back_populates="user")
