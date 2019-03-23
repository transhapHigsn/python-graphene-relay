from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from database import Base

class Email(Base):
    __tablename__ = 'email'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'), nullable=False)

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    # emails = relationship('email', back_populates='person')
    emails = relationship(
        Email,
        backref=backref('person',
                        uselist=False,
                        cascade='delete,all'))

class Persons(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    last = Column(String, nullable=False)
