#!/usr/bin/python3
"""Script to create the State "California" with the City "San Francisco" using SQLAlchemy"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Extract arguments
    username, password, database = sys.argv[1:]

    # Create engine and bind session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create State object for "California"
    california = State(name="California")

    # Create City object for "San Francisco" and link it to the State
    san_francisco = City(name="San Francisco", state=california)

    # Add City to the State's cities relationship
    california.cities.append(san_francisco)

    # Add State and City objects to the session and commit changes
    session.add(california)
    session.commit()

    # Close the session
    session.close()
