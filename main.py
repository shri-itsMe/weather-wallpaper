# # https://www.weatherapi.com/docs/ = API docs

import os
from dotenv import load_dotenv
import requests
import json

WEATHER_URL = "http://api.weatherapi.com/v1/current.json"
LOCATION_URL = "http://ip-api.com/json/{query}?fields=status,message,country,countryCode,regionName,city,timezone,query"







# PARAMS = {'key': api_key,
#         'q': "Grand Rapids"} #TODO: Get IP Address (seperate file?)

# load_dotenv()
# # API URL Endpoint for Current Weather; Parameter for Location

# api_key = os.getenv("WEATHER_API_KEY")
# if not api_key:
#     raise Exception("donde esta api key?")




# r = requests.get(url = URL, params = PARAMS)

# data = r.json()

# # print(data)
# print(data["current"]["temp_f"])
# print(data["current"]["condition"]["text"])

# # plan
# # figure out how osascript works
# # get it to change wall paper
# # link it all together


