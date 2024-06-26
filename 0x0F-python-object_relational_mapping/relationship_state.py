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

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    name = Column(String(128), nullable=True)

    # Define relationship to City with cascade delete
    cities = relationship('City', back_populates='state',
                          cascade='all, delete-orphan')

    # Import the City class at method level to resolve circular import issues
    @staticmethod
    def deferred_import():
        global City
        from relationship_city import City


# Perform the deferred import
State.deferred_import()
