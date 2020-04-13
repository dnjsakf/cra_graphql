from mongoengine import connect
from api.graphql.models import RankModel

MONGO_DTATBASE="graphene-mongo-example"
MONGO_HOST="mongomock://localhost"

connect(MONGO_DTATBASE, host=MONGO_HOST, alias="default")

def init_db():
  rank = RankModel(name="heo", mode="4x4", score=16, isMobile=False, reg_dttm="20200401170848")
  rank.save()

  rank = RankModel(name="kim", mode="4x4", score=2, isMobile=False, reg_dttm="20200401170848")
  rank.save()

  rank = RankModel(name="choi", mode="4x4", score=128, isMobile=False, reg_dttm="20200401170848")
  rank.save()

  rank = RankModel(name="lee", mode="4x4", score=1024, isMobile=False, reg_dttm="20200401170848")
  rank.save()