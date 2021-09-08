from datetime import datetime
from mongoengine import Document
from mongoengine.fields import (
    DateTimeField, ReferenceField, StringField, GeoPointField, DecimalField
)

class Site(Document):
    meta = {'collection': 'site'}
    site_id = StringField()
    name = StringField()
    location = GeoPointField()

class SurfaceObservation(Document):
    site = ReferenceField(Site)
    observation_time = StringField()
    air_temperature = DecimalField()
    dewpoint = DecimalField()
    relative_humidity = DecimalField()
    wind_chill = DecimalField()
    heat_index = DecimalField()
    wind_direction = StringField()
    wind_speed = DecimalField()
    wind_gust = DecimalField()
    pressure = DecimalField()
    rain = DecimalField()
