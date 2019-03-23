from database import db_session
from models import Person, Email

def create_person(name, age, mail):
    person = Person(name=name, age=age)
    db_session.add(person)
    db_session.flush()

    email = Email(email=mail, person_id=person.id)
    db_session.add(email)

    db_session.commit()
    return person, 'True', mail