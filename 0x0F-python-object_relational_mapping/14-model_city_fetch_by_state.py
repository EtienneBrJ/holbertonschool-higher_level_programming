#!/usr/bin/python3
"""
    Script that prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main(mysql_user, mysql_password, mysql_db):
    """
    Script that prints all City objects from the database hbtn_0e_14_usa
    Args:
        mysql_user: MySQL username.
        mysql_password: MySQL password.
        mysql_db: MySQL Database name.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        mysql_user, mysql_password, mysql_db), pool_pre_ping=True
        )

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(City, State).filter(
        State.id == City.state_id
    ).order_by(City.id)

    for city, state in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
