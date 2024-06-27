#!/usr/bin/python3
"changes the name of a State object from the database hbtn_0e_6_usa"

if __name__ == '__main__':
    "do not run if imported"
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys
    from model_state import Base, State

    argv = sys.argv
    if len(argv) == 4:
        user = argv[1]
        password = argv[2]
        db_name = argv[3]
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(user, password, db_name))
        Session = sessionmaker(bind=engine)
        session = Session()
        state = session.query(State).filter_by(id=2).first()
        state.name = 'New Mexico'
        session.commit()
        session.close()
