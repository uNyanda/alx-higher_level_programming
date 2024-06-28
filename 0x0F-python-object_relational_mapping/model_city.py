#!/usr/bin/python3
"""
This script contains the class definition of a city
that inherits from Base
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from model_state import Base, State


class City(Base):
    """
    Class definition for the State model in SQLAlchemy.

    This class represents a state entity, mapping to the 'states'
    table in a MySQL database
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # Define relationship to State
    state = relationship('State', back_populates='cities')
