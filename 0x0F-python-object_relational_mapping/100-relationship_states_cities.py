#!/usr/bin/python3
"""
This script creates the state 'California' with the city
'San Francisco' from the database hbtn_0e_100_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
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
        # Bnd the engine to the metadata of the Base class
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        new_state = State(name='California')
        new_city = City(name='San Francisco')
        new_state.cities.append(new_city)

        session.add(new_state)
        session.commit()

        session.close()
    except Exception as e:
        print(f'Error: {e}')
