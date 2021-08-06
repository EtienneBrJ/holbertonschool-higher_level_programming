#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost/{}'\
             .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db_uri, pool_pre_ping=True)
    Base.metadata.create_all(engine)
