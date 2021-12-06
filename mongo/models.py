from datetime import datetime
from mongoengine import Document

from mongoengine.fields import (
    DateTimeField, DictField, ReferenceField, StringField, PointField, DecimalField, ListField
)


class Site(Document):
    meta = {'collection': 'site'}
    site_ID = StringField()
    latitude = DecimalField()
    longitude = DecimalField()
    name = StringField()


class SurfaceObservation(Document):
    site = ReferenceField(Site)
    observation_time = StringField()
    uploaded_at = DateTimeField()
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


# TODO: Setup model schema for when Open Weather Map API can be implemented.
'''
class Hourly(Document):
    time = StringField()
    temp = DecimalField('temp')


class SurfaceForecast(Document):
    hourly = DictField(ReferenceField(Hourly))
'''
