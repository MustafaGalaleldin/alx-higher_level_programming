#!/usr/bin/python3
"""prints the State object with the name passed as argument
from the database hbtn_0e_6_usa"""

if __name__ == '__main__':
    "do not run if imported"
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys
    from model_state import Base, State

    argv = sys.argv
    if len(argv) == 5:
        user = argv[1]
        password = argv[2]
        db_name = argv[3]
        state_name = argv[4]
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(user, password, db_name))
        Session = sessionmaker(bind=engine)
        session = Session()
        states = session.query(State).all()
        existed = 0
        for state in states:
            if state.name == state_name:
                print(state.id)
                existed = 1
                break
        if not existed:
            print('Not found')
        session.close()
