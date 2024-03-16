#!/usr/bin/python3
"""Script that prints the first State object from the database"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State, Base


if __name__ == "__main__":
    # Extract arguments
    username, password, database = sys.argv[1:]

    # Create engine and bind session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database))
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the first State objects and sort by id
    first_state = session.query(State).order_by(State.id).first()

    # Check if a State object was found
    if first_state is not None:
        print('{}: {}'.format(first_state.id, first_state.name))
    else:
        print('Nothing')

    # Close the session
    session.close()
