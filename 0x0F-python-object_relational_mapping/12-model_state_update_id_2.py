#!/usr/bin/python3
"""
This script changes the name of a state object
from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    usr = sys.argv[1]
    pwd = sys.argv[2]
    dtb = sys.argv[3]

    try:
        engine = create_engine(
            f'mysql+mysqldb://{usr}:{pwd}@localhost:3306/{dtb}'
        )
        Session = sessionmaker(bind=engine)
        session = Session()

        state = session.query(State).filter(State.id == 2).first()

        if state:
            state.name = "New Mexico"
            session.commit()

        session.close()
    except Exception as e:
        print(f'Error: {e}')
