#!/usr/bin/python3
"""lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa"""

if __name__ == '__main__':
    "do not run if imported"
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys
    from model_state import Base, State

    argv = sys.argv
    if len(argv) == 4:
        name = argv[1]
        password = argv[2]
        db_name = argv[3]
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(name, password, db_name))
        Session = sessionmaker(bind=engine)
        session = Session()
        states = session.query(State).order_by(State.id)
        for state in states:
            if 'a' in state.name:
                print(f"{state.id}: {state.name}")
        session.close()
