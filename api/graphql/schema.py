from datetime import datetime
import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from api.graphql.models import Department as DepartmentModel
from api.graphql.models import Employee as EmployeeModel
from api.graphql.models import Role as RoleModel
from api.graphql.models import GameRanking as GameRankingModel


class Department(MongoengineObjectType):
  class Meta:
    model = DepartmentModel
    interfaces = (Node,)

class Role(MongoengineObjectType):
  class Meta:
    model = RoleModel
    interfaces = (Node,)

class Employee(MongoengineObjectType):
  class Meta:
    model = EmployeeModel
    interfaces = (Node,)

class GameRanking(MongoengineObjectType):
  class Meta:
    model = GameRankingModel
    interfaces = (Node,)

  def resolve_reg_dttm(parent, info):
    return datetime.strptime(parent.reg_dttm, "%Y%m%d%H%M%S").strftime("%Y-%m-%d %H:%M:%S")

class Query(graphene.ObjectType):
  node = Node.Field()
  all_employees = MongoengineConnectionField(Employee)
  all_role = MongoengineConnectionField(Role)
  role = graphene.Field(Role)
  ranking = MongoengineConnectionField(GameRanking)

schema = graphene.Schema(query=Query, types=[Department, Employee, Role, GameRanking])