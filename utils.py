from database import db_session
from models import Person, Email

def create_person(name, age, mail):
    output = {
        'person': None,
        'ok': False,
        'mail': mail,
        'message': ''
    }
    person = db_session.query(Person).filter(
        Person.name == name,
        Person.age == age,
    ).order_by(Person.id.desc()).first()

    if person:
        output.update({
            'person': person,
            'message': 'Person already added.'
        })
        return output

    mail_parts = mail.split('@')
    if len(mail_parts) != 2:
        output.update({
            'message': 'Incorrect mail provided.'
        })
        return output

    username, domain = mail_parts
    domain_parts = domain.split('.')
    if len(domain_parts) != 2:
        output.update({
            'message': 'Incorrect mail provided.'
        })
        return output

    person = Person(name=name, age=age)
    db_session.add(person)
    db_session.flush()

    email = Email(email=mail, person_id=person.id)
    db_session.add(email)

    db_session.commit()
    output.update({
        'ok': True,
        'person': person,
        'message': 'Person added successfully.'
    })
    return output