#!/usr/bin/python3
"Updated City"

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    "class to define cities objects and manipulate their table"
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, unique=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship('State', back_populates='cities')
