#!/usr/bin/python3
"a script that lists all State objects from the database hbtn_0e_6_usa"

if __name__ == '__main__':
    "do not run if imported"
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
        for a_state in session.query(State).all():
            print("{}: {}".format(a_state.id, a_state.name))
        session.close()
