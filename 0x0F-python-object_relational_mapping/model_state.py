#!/usr/bin/python3
"""This script starts a link class to a table in the database"""
import sys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class State(Base):
    """
    Class definition for the State model in SQLAlchemy.

    This class represents a state entity, mapping to the 'states'
    table in a MySQL database
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    # Define relationship to City
    cities = relationship('City', back_populates='state')


if __name__ == "__main__":
    # Check for correct arguments
    if len(sys.argv) != 4:
        print("Usage {} <username> <password> <database>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Gather the arguments
    usr = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine
    engine = create_engine(f"mysql+mysqldb://{usr}:\
        {password}@localhost:3306/{database}",
                           pool_pre_ping=True)

    # Create table in the database
    Base.metadata.create_all(engine)
