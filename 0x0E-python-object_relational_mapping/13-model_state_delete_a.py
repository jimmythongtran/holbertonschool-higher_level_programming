#!/usr/bin/python3
'''
This is the '13-model_state_delete_a' module

This writes a script deletes all State objects with names containing letter a
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

    for entryDeletion in session.query(State).filter(State.name.like('%a%')):
        session.delete(entryDeletion)
        session.commit()
