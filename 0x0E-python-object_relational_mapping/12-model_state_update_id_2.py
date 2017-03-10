#!/usr/bin/python3
'''
This is the '12-model_state_update_id_2' module

This writes a script changes the name of a State object from database
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

    for entryUpdate in session.query(State).filter(State.id == 2):
        entryUpdate.name = 'New Mexico'
        session.commit()
