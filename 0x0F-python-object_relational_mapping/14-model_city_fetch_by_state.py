#!/usr/bin/python3
"""Fetch All cities using sqlalchemy"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def fetch_all_cities():
    """Fetch all states using sqlalchemy"""
    # create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the table and fetch data
    cities = session.query(State, City).join(City)
    for city, state in cities:
        print(f"{state.name}: ({city.id}): {city.name}")


if __name__ == "__main__":
    fetch_all_cities()
