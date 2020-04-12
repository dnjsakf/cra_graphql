from datetime import datetime
from mongoengine import Document
from mongoengine.fields import (
    DateTimeField, ReferenceField, StringField, BooleanField, IntField
)

class Department(Document):
    meta = {'collection': 'department'}
    name = StringField()

class Role(Document):
    meta = {'collection': 'role'}
    name = StringField()

class Employee(Document):
    meta = {'collection': 'employee'}
    name = StringField()
    hired_on = DateTimeField(default=datetime.now)
    department = ReferenceField(Department)
    role = ReferenceField(Role)

class GameRanking(Document):
    meta = {'collection': 'game_ranking'}
    name = StringField()
    mode = StringField()
    score = IntField()
    reg_dttm = StringField()
    isMobile = BooleanField()