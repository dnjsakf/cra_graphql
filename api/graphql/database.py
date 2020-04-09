# flask_graphene_mongo/database.py
from mongoengine import connect

from api.graphql.models import Department, Employee, Role

# You can connect to a real mongo server instance by your own.
connect('graphene-mongo-example', host='mongomock://localhost', alias='default')


def init_db():
    # Create the fixtures
    engineering = Department(name='Engineering')
    engineering.save()

    hr = Department(name='Human Resources')
    hr.save()

    manager = Role(name='manager')
    manager.save()

    engineer = Role(name='engineer')
    engineer.save()

    peter = Employee(name='Peter', department=engineering, role=engineer)
    peter.save()

    roy = Employee(name='Roy', department=engineering, role=engineer)
    roy.save()

    tracy = Employee(name='Tracy', department=hr, role=manager)
    tracy.save()