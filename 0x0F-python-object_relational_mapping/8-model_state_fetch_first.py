#!/usr/bin/python3
"prints the first State object from the database hbtn_0e_6_usa"

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
        state = session.query(State).first()
        if state:
            print(f"{state.id}: {state.name}")
        else:
            print('Nothing')
        session.close()
