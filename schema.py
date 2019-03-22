from graphene import ObjectType, Schema, String, ID, Int, Field, Mutation, Boolean, Argument
from models import Person as PersonModel

from graphene.relay import Node, Connection
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType, utils


class Person(SQLAlchemyObjectType):
    class Meta:
        model = PersonModel
        interfaces = (Node, )


class PersonConnection(Connection):
    class Meta:
        node = Person


SortEnumPerson = utils.sort_enum_for_model(PersonModel, 'SortEnumPerson',
    lambda c, d: c.upper() + ('_ASC' if d else '_DESC'))


class Query(ObjectType):
    node = Node.Field()
    all_persons = SQLAlchemyConnectionField(
        PersonConnection,
        sort=Argument(
            SortEnumPerson,
            default_value=utils.EnumValue('id_asc', PersonModel.id.asc())))


class CreatePerson(Mutation):
    class Arguments:
        name = String()

    ok = Boolean()
    person = Field(lambda: Person)

    def mutate(self, info, name):
        person = Person(name=name)
        ok = True
        return CreatePerson(person=person, ok=ok)

class MyMutations(ObjectType):
    create_person = CreatePerson.Field()


schema = Schema(query=Query, mutation=MyMutations, types=[Person])