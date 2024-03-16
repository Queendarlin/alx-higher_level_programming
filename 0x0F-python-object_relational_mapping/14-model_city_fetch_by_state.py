#!/usr/bin/python3
"""Script that fetches all City objects from the database"""

from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State, Base
from model_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects and sort by id
    cities = session.query(City, State).join(State)

    for city, state in cities.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.commit()

    # Close the session
    session.close()
