from database import db_session
from models import Person

def create_person(name, age):
    person = Person(name=name, age=age)
    db_session.add(person)
    db_session.commit()
    return person