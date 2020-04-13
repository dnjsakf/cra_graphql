import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField

from api.graphql.models import RankModel, RankType
from api.graphql.mutation import InsertRank, UpdateRank, DeleteRank
    
class Mutation(graphene.ObjectType):
  insert_rank = InsertRank.Field()
  update_rank = UpdateRank.Field()
  delete_rank = DeleteRank.Field()


class Query(graphene.ObjectType):
  all_ranks = MongoengineConnectionField(RankType)
  
  ranks = graphene.List(RankType, **{
    "mode": graphene.String(required=True), 
    "limit": graphene.Int(), 
    "skip": graphene.Int()
  })
  rank = graphene.Field(RankType, **{
    "id": graphene.String(required=True)
  })

  def resolve_ranks(parent, info, mode, **kwargs):
    return RankModel.objects(mode=mode).skip(kwargs.get("skip")).limit(kwargs.get("limit"))

  def resolve_rank(parent, info, id):
    return RankModel.objects.get(id=id)

schema = graphene.Schema(
  query=Query,
  mutation=Mutation,
  types=[RankType]
)