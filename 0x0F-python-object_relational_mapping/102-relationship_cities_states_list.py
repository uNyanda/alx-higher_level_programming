#!/usr/bin/python3
"""
This script lists all City objects from the database hbtn_0e_101_usa
In the format <city id>: <city name> -> <state name>
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
            f'mysql+mysqldb://{user}:{pswd}@localhost:3306/{dtbs}',
            pool_pre_ping=True
        )

        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        cities = session.query(City).order_by(City.id).all()

        for city in cities:
            print(f'{city.id}: {city.name} -> {city.state.name}')

        session.close()

    except Exception as e:
        print(f'Error: {e}')
