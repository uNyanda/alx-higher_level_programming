#!/usr/bin/python3
"""
This script contains a class definition of a city that
inherits from Base
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):
    """
    Defines a City class that inherits
    from the Base class
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id', ondelete='CASCADE'),
                      nullable=False)

    # Define relationship to State
    state = relationship('State', back_populates='cities')
