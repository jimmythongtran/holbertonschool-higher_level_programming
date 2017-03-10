#!/usr/bin/python3
'''
This is the '11-model_state_insert' module

This writes a script that adds State object "Louisiana" to the database
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
    newEntry = State(name='Louisiana')
    session.add(newEntry)
    session.commit()

    for entry in session.query(State).filter(State.name == "Louisiana"):
        print("{}".format(entry.id))
