# Set up IP Location
# https://ip-api.com/docs/api:json = API Docs
# No Key needed
import requests

class Location:
    def __init__(self, url):
        self.url = url

    def location_getter():
        r = requests.get(url = self.url, params = "")
        data = r.json()

        return data
    
    def get_city(self):
        return self.location_getter()["city"]

