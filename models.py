from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import backref, relationship

from database import Base


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)