#!/usr/bin/python3
"""Script that deletes all State objects with a name
containing 'a' from the database"""
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

    # Query State objects containing 'a'
    state_with_a = session.query(State).filter(State.name.like('%a%')).all()

    # Delete the State objects
    for state in state_with_a:
        session.delete(state)
    # Commit the session to save changes to the database
    session.commit()

    # Close the session
    session.close()
