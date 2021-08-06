#!/usr/bin/python3
""" Prints all the city objects from the database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost/{}'\
             .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db_uri, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    s = Session()

    for state, city in s.query(State, City)\
                        .filter(City.state_id == State.id)\
                        .order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    s.close()