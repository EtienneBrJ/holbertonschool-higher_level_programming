#!/usr/bin/python3
""" Prints all the city objects from the database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.schema import Table
from sqlalchemy.orm import Session


if __name__ == "__main__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost/{}'\
             .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db_uri, pool_pre_ping=True)

    Base.metadata.create_all(engine)
    s = Session(engine)

    new_city = City(name='San Francisco')
    new_state = State(name='California')
    new_state.cities.append(new_city)

    s.add_all([new_state, new_city])
    s.commit()

    s.close()
