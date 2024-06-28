#!/usr/bin/python3
"""Updated state"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    "class to define state objects and manipulate their table"
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates='state',cascade='all')
