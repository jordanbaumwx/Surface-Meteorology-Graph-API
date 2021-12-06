from collections import namedtuple
import requests
import json
import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from mongo.models import Site as SiteModel
from mongo.models import SurfaceObservation as SurfaceObservationModel
from mongo.models import SurfaceForecast as SurfaceForecastModel


class Site(MongoengineObjectType):
    class Meta:
        model = SiteModel
        interfaces = (Node,)


class SurfaceObservation(MongoengineObjectType):
    class Meta:
        model = SurfaceObservationModel
        interfaces = (Node,)


# TODO: Set up the Site Forecast connection information.
'''
class SiteForecast(MongoengineObjectType):
    class Meta:
        model = SurfaceForecastModel
        interfaces = (Node, )
'''


def _json_object_hook(d):
    return namedtuple('X', d.keys())({*d.values()})


def json2obj(data):
    return json.loads(data, object_hook=_json_object_hook)


# TODO: Wrap the openweather map API to graphql
def open_weather_map_api(lat, lon):
    url = 'https://api.openweathermap.org/data/2.5/onecall?lat=' + str(lat) + '&lon=' + \
        str(lon) + '&exclude=hourly,daily,alerts&appid={API_KEY}'
    print(requests.get(url).text)


class Query(graphene.ObjectType):
    node = Node.Field()
    sites = MongoengineConnectionField(Site)
    surface_observations = MongoengineConnectionField(SurfaceObservation)

    # TODO: Add in the forecast query
    '''
    site_forecasts = MongoengineConnectionField(
        SiteForecast, lat=graphene.Float(required=True), lon=graphene.Float(required=True))

    def resolve_site_forecasts(self, args, lat, lon):
        site_forecasts = open_weather_map_api(
            lat, lon)
    '''


schema = graphene.Schema(query=Query, types=[SurfaceObservation, Site])
