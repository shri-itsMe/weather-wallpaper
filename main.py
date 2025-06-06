# https://www.weatherapi.com/docs/ = API docs

import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv("WEATHER_API_KEY")
if not api_key:
    raise Exception("donde esta api key?")


# API URL Endpoint for Current Weather; Parameter for Location
URL = "http://api.weatherapi.com/v1/current.json"
PARAMS = {'key': api_key,
        'q': "Grand Rapids"} #TODO: Get IP Address (seperate file?)

r = requests.get(url = URL, params = PARAMS)

data = r.json()

print(data)
