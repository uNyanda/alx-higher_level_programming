#!/usr/bin/python3
"""
This script deletes all state objects with a name containing the
letter a from the database htbn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    user = sys.argv[1]
    pswd = sys.argv[2]
    dtbs = sys.argv[3]

    try:
        engine = create_engine(
            f'mysql+mysqldb://{user}:{pswd}@localhost:3306/{dtbs}'
        )
        Session = sessionmaker(bind=engine)
        session = Session()

        state_with_a = session.query(State).filter(
            State.name.like('%a%')).all()

        for state in state_with_a:
            session.delete(state)

        session.commit()
        session.close()
    except Exception as e:
        print(f'Error: {e}')
