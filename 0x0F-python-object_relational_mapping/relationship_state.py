#!/usr/bin/python3
"""
This script contains a class definition of state
that inherits from Base
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    Class definition of a state object
    that inherits from Base
    """
    __tablename__ = 'states'
    from relationship_city import City

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    name = Column(String(128), nullable=True)

    # Define relationship to City with scade delete
    cities = relationship('City', back_populates='state',
                          cascade='all, delete-orphan')
