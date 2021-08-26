from sqlalchemy import (
    Column, 
    String, 
    Integer, 
    Boolean,
    ForeignKey
)
from sqlalchemy.orm import relationship

import database


class Blog(database.Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    description = Column(String)
    available = Column(Boolean, default=True)

    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship('User', back_populates='blogs')