#!/usr/bin/python3
"""
This script prints all city objects from the database
hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
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

        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        cities = session.query(City).join(State).order_by(City.id).all()

        for city in cities:
            print(f'{city.state.name}: ({city.id}) {city.name}')

        session.close()

    except Exception as e:
        print(f'Error: {e}')
