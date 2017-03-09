#!/usr/bin/python3
'''
This is the '9-model_state_fetch_first' module

This prints all the State objects from the database hbtn_0e_6_usa
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for entry in session.query(State).filter(State.name.like('%a%')):
        print("{}: {}".format(entry.id, entry.name))
