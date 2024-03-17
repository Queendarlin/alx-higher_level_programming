#!/usr/bin/python3
"""Script to create the State "California" with the City "San Francisco"""

from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    add_state = State(name='California')
    add_city = City(name='San Francisco')
    add_state.cities.append(add_city)

    session.add(add_state)
    session.add(add_city)
    session.commit()

    # Close the session
    session.close()
