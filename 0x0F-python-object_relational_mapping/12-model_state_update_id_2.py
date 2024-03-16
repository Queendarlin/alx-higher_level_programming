#!/usr/bin/python3
"""Script that adds the State object "Louisiana" to the database"""

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

    # Query the State object with id = 2
    update_state = session.query(State).filter_by(id=2).first()

    # Update the name of the State object
    if update_state:
        update_state.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
