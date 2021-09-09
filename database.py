from mongoengine import connect
import requests

from mongo.models import Site, SurfaceObservation
from mongoengine.fields import (
    DateTimeField, ReferenceField, StringField, PointField, DecimalField
)


# Mongo DB Connection String
connect('sample-ok-mesonet', host='mongomock://localhost', alias='default')

def fetch_csv_from_url(url="http://www.mesonet.org/data/public/mesonet/current/current.csv.txt"):
    r = requests.get(url)
    if r.status_code != 200:
        raise Exception("Could not fetch from URL: %s" % url)
    
    # Get every row except the header row (1st row)
    station_rows = r.text.split('\n')[1:-1]
    station_data = []
    for row in station_rows:
        row = row.split(',')
        data = {
            "station_id": row[0],
            "site_name": row[1] + ", " + row[2],
            "site_coordinates": { "type": "Point", "coordinates": [ row[4], row[3] ] },
            "latitude": row[3],
            "longitude": row[4],
            "observation_time": row[5] + "-" + row[6] + "-" + row[7] + "T" + row[8] + ":" + row[9],
            "air_temperature": row[-12],
            "dewpoint": row[-11],
            "relative_humidity": row[-10],
            "wind_chill": row[-9],
            "heat_index": row[-8],
            "wind_direction": row[-7],
            "wind_speed": row[-6],
            "wind_gust": row[-5],
            "pressure": row[-4], 
            "maximum_temperature": row[-3],
            "minimum_temperature": row[-2],
            "rain": row[-1]
        }
        station_data.append(data)

    return station_data

from datetime import datetime
def init_db():
    station_data = fetch_csv_from_url()
    for data in station_data:
        location = PointField()
        location.location = data["site_coordinates"]

        site = Site(site_ID=data["station_id"], name=data["site_name"], latitude=data['latitude'], longitude=data['longitude'] )
        site.save()

    
        try:
            
            surface_ob = SurfaceObservation(site=site, 
                observation_time = data['observation_time'],
                air_temperature = float(data['air_temperature']),
                dewpoint = float(data['dewpoint']),
                relative_humidity = float(data['relative_humidity']),

                wind_direction = data['wind_direction'],
                wind_speed = float(data['wind_speed']),
                wind_gust = float(data['wind_gust']),
                pressure = float(data['pressure']),
                uploaded_at = datetime.now(),

            )
            surface_ob.save()
        except:
            pass



