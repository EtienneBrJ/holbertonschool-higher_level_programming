#!/usr/bin/python3
""" Class definition of a State and an instance Base = declarative_base():
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """ Class state
    """
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, nullable=False,
                unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
