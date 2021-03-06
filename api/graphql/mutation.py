import graphene
from api.graphql.models import RankModel, RankType
from datetime import datetime

# Mutations
class RankInupt(graphene.InputObjectType):
  mode = graphene.String(required=True)
  name = graphene.String(required=True)
  score = graphene.Int(required=True)
  is_mobile = graphene.Boolean(required=True)
  reg_dttm = graphene.String(default_value=datetime.now().strftime("%Y%m%d%H%M%S"))

class InsertRank(graphene.Mutation):
  class Arguments:
    data = RankInupt(required=True)  # Single
    #data = graphene.List(RankInupt) # Multiple

  Output = RankType
  #rank = graphene.Field(RankType) # return naming output

  def mutate(root, info, data=None):
    model = RankModel(
      mode=data.mode,
      name=data.name,
      score=data.score,
      is_mobile=data.is_mobile,
      reg_dttm=data.reg_dttm
    )
    model.save()
    
    return model
    #return InsertRank(rank=rank) # return naming output

class UpdateRank(graphene.Mutation):
  rank = graphene.Field(RankType)
  success = graphene.Boolean()
  
  class Arguments:
    mode = graphene.String(required=True)
    name = graphene.String(required=True)
    score = graphene.Int()
    is_mobile = graphene.Boolean()

  def mutate(root, info, mode, name, score=None, is_mobile=None,):
    model = RankModel.objects(mode=mode, name=name).first()
    
    if score is not None:
      model.score = score
    
    if is_mobile is not None:
      model.is_mobile = is_mobile
      
    model.save()
    
    return UpdateRank(rank=model, success=True)

class DeleteRank(graphene.Mutation):
  success = graphene.Boolean()
  
  class Arguments:
    mode = graphene.String(required=True)
    name = graphene.String(required=True)

  @classmethod
  def mutate(cls, root, info, mode, name):
    RankModel.objects(mode=mode, name=name).delete()
    
    success = RankModel.objects(mode=mode, name=name).first() == None
    
    return cls(success=success)