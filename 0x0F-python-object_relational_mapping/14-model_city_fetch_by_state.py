#!/usr/bin/python3
"prints all City objects from the database hbtn_0e_14_usa"

from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City

argv = sys.argv
if len(argv) == 4:
    user = argv[1]
    password = argv[2]
    db_name = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, password, db_name))
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    cities = session.query(City).order_by(City.id).all()
    states = session.query(State).all()
    for city in cities:
        state = session.query(State).filter_by(id=city.state_id).first()
        print(f"{state.name}: ({city.id}) {city.name}")
