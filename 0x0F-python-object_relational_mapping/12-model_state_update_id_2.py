#!/usr/bin/python3
"""Fetch All states using sqlalchemy"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def filter_states():
    """Fetch all states using sqlalchemy"""
    # create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # create state instance
    state_to_update = session.query(State).filter(State.id == 2).first()
    if (state_to_update.id):
        state_to_update.name = "New Mexico"
        # commit session memory to db
        session.commit()


if __name__ == "__main__":
    filter_states()
