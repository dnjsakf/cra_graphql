import graphene
from graphene.relay import Node

from api.graphql.models import RankModel, RankType
from api.graphql.mutations import InsertRank, UpdateRank, DeleteRank

from datetime import datetime
    
class Mutation(graphene.ObjectType):
  insert_rank = InsertRank.Field()
  update_rank = UpdateRank.Field()
  delete_rank = DeleteRank.Field()


class Query(graphene.ObjectType):
  node = Node.Field()

  ranks = graphene.List(RankType, mode=graphene.String(required=True))
  rank = graphene.Field(RankType, id=graphene.String(required=True))

  def resolve_ranks(parent , info, mode):
    return RankModel.objects(mode=mode)

  def resolve_rank(parent , info, id):
    return RankModel.objects.get(id=id)

schema = graphene.Schema(
  query=Query,
  mutation=Mutation,
  types=[RankType]
)