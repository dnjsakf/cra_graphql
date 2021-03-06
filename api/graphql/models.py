import datetime

from graphene.relay import Node

from mongoengine import Document
from mongoengine.fields import StringField, BooleanField, IntField

from graphene_mongo import MongoengineObjectType

# Models
class RankModel(Document):
  meta = {'collection': 'game_ranking'}
  mode = StringField()
  name = StringField()
  score = IntField()
  is_mobile = BooleanField()
  reg_dttm = StringField()
  upd_dttm = StringField()
  

# ObjectTypes
class RankType(MongoengineObjectType):
  class Meta:
    model = RankModel
    interfaces = (Node,)

  def resolve_reg_dttm(parent, info, **kwargs):
    return datetime.datetime.strptime(parent.reg_dttm, "%Y%m%d%H%M%S").strftime("%Y-%m-%d %H:%M:%S")
