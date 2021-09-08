import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models import Site as SiteModel
from models import SurfaceObservation as SurfaceObservationModel


class Site(MongoengineObjectType):
    class Meta:
        model = SiteModel
        interfaces = (Node,)


class SurfaceObservation(MongoengineObjectType):
    class Meta:
        model = SurfaceObservationModel
        interfaces = (Node,)


class Query(graphene.ObjectType):
    node = Node.Field()
    sites = MongoengineConnectionField(Site)
    surface_observations = MongoengineConnectionField(surface_observation)

schema = graphene.Schema(query=Query, types=[SurfaceObservation, Site])
