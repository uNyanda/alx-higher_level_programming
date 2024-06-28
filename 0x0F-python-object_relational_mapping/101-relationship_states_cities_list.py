#!/usr/bin/python3
"""
This script lists all state objects, and corresponding city objects
contained in the database hbtn_0e_101_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City
import sys


if __name__ == "__main__":
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
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        states = session.query(State).order_by(State.id).all()

        # Loop through each state and its cities to print the required format
        for state in states:
            print(f'{state.id}: {state.name}')
            for city in state.cities:
                print(f'\t{city.id}: {city.name}')

        session.close()
    except Exception as e:
        print(f'Error: {e}')
