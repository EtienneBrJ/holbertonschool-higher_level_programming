#!/usr/bin/python3
""" Class definition of a State and an instance Base = declarative_base():
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """ Class state
    """
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, primary_key=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state')
