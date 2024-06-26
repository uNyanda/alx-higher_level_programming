#!/usr/bin/python3
"""This script lists all State objects that contain
the letter a from the database hbtn_0e_6_usa
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

    # Create the engine and bind to session
    try:
        engine = create_engine(
            f'mysql+mysqldb://{usr}:{pwd}@localhost:3306/{dtb}'
	)
	    Session = sessionmaker(bind=engine)
	    session = Session()

        # Query State objects containing 'a' in their name, sorted by id
        states_with_a = session.query(State).filter(
            State.name.like('%a')).order_by(State.id).all()

        # Print the result
        if states_with_a:
            for state in states_with_a:
                print(f'{state.id}: {state.name}')
        else:
            print('Nothing')

        # Close the session
        session.close()
    except Exception as e:
        print(f'Error: {e}')

