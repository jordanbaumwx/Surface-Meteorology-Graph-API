from mongoengine import connect

from models import Site, SurfaceObservation

# Mongo DB Connection String
connect('sample-ok-mesonet', host='mongomock://localhost', alias='default')


def init_db():
    pass
