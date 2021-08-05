#!/usr/bin/python3
""" Changes the name of a State object from the database
"""
import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost/{}'\
             .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db_uri, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    s = Session()

    for state in s.query(State).filter(State.id == 2):
        state.name = 'New Mexico'

    s.commit()
    s.close()
