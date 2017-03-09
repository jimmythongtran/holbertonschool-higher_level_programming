#!/usr/bin/python3
'''
This is the '10-model_state_my_get' module

This prints the State object with the name passed as argument from the database
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

    entry = session.query(State).filter(State.name == sys.argv[4]).first()
    if entry is not None:
        print("{}".format(entry.id))
    else:
        print("Not found")
