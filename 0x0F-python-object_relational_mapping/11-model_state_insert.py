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

    # Create a new State object for Louisiana
    louisiana = State(name="Louisiana")

    # Add the new State object to the session
    session.add(louisiana)

    # Commit the session to save changes to the database
    session.commit()

    # Print the new states.id after creation
    print(louisiana.id)

    # Close the session
    session.close()
