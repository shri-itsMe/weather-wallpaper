# Set up IP Location
# https://ip-api.com/docs/api:json = API Docs
# No Key needed
LOCATION_URL = "http://ip-api.com/json/?fields=status,message,country,countryCode,regionName,city,timezone,query"

import requests

class Location:
    def __init__(self, url=LOCATION_URL):
        self.url = url

    def location_getter(self):
        r = requests.get(url = self.url)
        # r = requests.get(url = self.urL)
        data = r.json()

        return data
    
    def get_city(self):
        return self.location_getter()["city"]

