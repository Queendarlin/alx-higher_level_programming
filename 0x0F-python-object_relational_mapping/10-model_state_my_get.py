#!/usr/bin/python3
"""Script that prints the State object with the name passed as argument"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State, Base


if __name__ == "__main__":
    # Extract arguments
    username, password, database, state_name = sys.argv[1:]

    # Create engine and bind session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database))
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State object with the specified name
    state = session.query(State).filter(State.name == state_name).\
        first()

    # Print the result
    if state is not None:
        print('{}'.format(state.id))
    else:
        print('Not found')

    # Close the session
    session.close()
