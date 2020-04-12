# flask_graphene_mongo/database.py
from mongoengine import connect

from api.graphql.models import Department, Employee, Role, GameRanking

# You can connect to a real mongo server instance by your own.
MONGO_DTATBASE="graphene-mongo-example"
MONGO_HOST="mongomock://localhost"
connect(MONGO_DTATBASE, host=MONGO_HOST, alias="default")

def init_db():
    # Create the fixtures
    engineering = Department(name="Engineering")
    engineering.save()

    hr = Department(name="Human Resources")
    hr.save()

    manager = Role(name="manager")
    manager.save()

    engineer = Role(name="engineer")
    engineer.save()

    peter = Employee(name="Peter", department=engineering, role=engineer)
    peter.save()

    roy = Employee(name="Roy", department=engineering, role=engineer)
    roy.save()

    tracy = Employee(name="Tracy", department=hr, role=manager)
    tracy.save()

    rank = GameRanking(name="heo", mode="4x4", score=16, isMobile=False, reg_dttm="20200401170848")
    rank.save()

    rank = GameRanking(name="heo", mode="4x4", score=2, isMobile=False, reg_dttm="20200401170848")
    rank.save()

    rank = GameRanking(name="heo", mode="4x4", score=128, isMobile=False, reg_dttm="20200401170848")
    rank.save()

    rank = GameRanking(name="heo", mode="4x4", score=1024, isMobile=False, reg_dttm="20200401170848")
    rank.save()