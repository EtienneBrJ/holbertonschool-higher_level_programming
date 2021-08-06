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

    for row in s.query(State, City).join(City).order_by(City.id):
        print("{}: ({}) {}".format(row[0].name, row[1].id, row[1].name))

    s.commit()
    s.close()
