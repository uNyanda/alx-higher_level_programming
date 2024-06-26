#!/usr/bin/python3
"""
This script lists all State objects from database
hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Check for provided arguments
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Gather all arguments
    usr = sys.argv[1]
    pwd = sys.argv[2]
    dtb = sys.argv[3]

    # Create engine and bindto session
    engine = create_engine(f'mysql+mysqldb:\
        //{usr}:{pwd}@localhost:3306/{dtb}')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects and sort by id
    states = session.query(State).order_by(State.id).all()

    # Print the results
    for state in states:
        print(f"{state.id}:{state.name}")

    # Close the session
    session.close()
