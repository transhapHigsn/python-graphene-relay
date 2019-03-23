from graphene import ObjectType, Schema, String, ID, Int, Field, Mutation, Boolean, Argument
from models import Person as PersonModel
from models import Persons as PersonsModel

from graphene.relay import Node, Connection
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType, utils

from utils import create_person

class Person(SQLAlchemyObjectType):
    class Meta:
        model = PersonModel
        interfaces = (Node, )


class PersonConnection(Connection):
    class Meta:
        node = Person

class Persons(SQLAlchemyObjectType):
    class Meta:
        model = PersonsModel
        interfaces = (Node, )


class PersonsConnection(Connection):
    class Meta:
        node = Persons


SortEnumPerson = utils.sort_enum_for_model(PersonModel, 'SortEnumPerson',
    lambda c, d: c.upper() + ('_ASC' if d else '_DESC'))


class Query(ObjectType):
    node = Node.Field()
    all_persons = SQLAlchemyConnectionField(
        PersonConnection,
        sort=Argument(
            SortEnumPerson,
            default_value=utils.EnumValue('id_asc', PersonModel.id.asc())))
    all_next_person = SQLAlchemyConnectionField(PersonsConnection, sort=None)


class CreatePerson(Mutation):
    class Arguments:
        name = String()
        age = Int()

    ok = Boolean()
    person = Field(lambda: Person)

    def mutate(self, info, name, age):
        person = create_person(name, age)
        return CreatePerson(person=person, ok=True)


class MyMutations(ObjectType):
    create_person = CreatePerson.Field()


schema = Schema(query=Query, mutation=MyMutations, types=[Person])

# get all rows from person table
'''
{
    allPersons{
        edges{
            node{
                id
                name
                age
            }
        }
    }
}
'''

# add new row in person table
'''
mutation mut{
    createPerson(name: "Person Name", age: 11) {
            person{
                    id
                    name
                    age
            }
            ok
    }
} 
'''