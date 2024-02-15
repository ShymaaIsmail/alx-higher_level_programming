#!/usr/bin/python3
"""Fetch All states using sqlalchemy"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def fetch_first_states():
    """Fetch all states using sqlalchemy"""
    # create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the table and fetch data
    state = session.query(State).limit(1).first()
    if not state:
        print("Nothing")
    else:
        print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    fetch_first_states()
