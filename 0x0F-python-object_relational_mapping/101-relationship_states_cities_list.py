#!/usr/bin/python3
""" a script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""
import sys
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
        for city in session.query(City).\
                filter(state.id == City.state_id).order_by(City.id).all():
            print("    {}: {}".format(city.id, city.name))
    session.close()
