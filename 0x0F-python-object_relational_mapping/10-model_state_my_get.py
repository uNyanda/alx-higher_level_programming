#!/usr/bin/python3
"""
This script prints the State object with the name
passed as argument from database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Check for provided arguments
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state>"
              .format(sys.argv[0]))
        sys.exit(1)

    usr = sys.argv[1]
    pwd = sys.argv[2]
    dtb = sys.argv[3]
    sts = sys.argv[4]

    try:
        engine = create_engine(
            f'mysql+mysqldb://{usr}:{pwd}@localhost:3306/{dtb}'
        )
        Session = sessionmaker(bind=engine)
        session = Session()

        state = session.query(State).filter(State.name == sts).first()

        if state:
            print(state.id)
        else:
            print("Not found")

        session.close()

    except Exception as e:
        print(f'Error: {e}')
