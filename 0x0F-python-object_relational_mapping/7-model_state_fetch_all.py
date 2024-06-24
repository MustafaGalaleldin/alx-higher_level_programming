#!/usr/bin/python3
"a script that lists all State objects from the database hbtn_0e_6_usa"

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

argv = sys.argv
if len(argv) == 4:
    name = argv[1]
    password = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(name, password, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for n, a_state in enumerate(session.query(State).all(), start=1):
        print("{}: {}".format(n, a_state.name))
    session.close()
