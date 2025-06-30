import os
from dotenv import load_dotenv
import requests
import json

WEATHER_URL = "http://api.weatherapi.com/v1/current.json"

# # print(data)
# print(data["current"]["temp_f"])
class Weather:
    def __init__(self, location):
        self.location = location
        # API URL Endpoint for Current Weather; Parameter for Location

    def weather_getter(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        dotenv_path = os.path.join(script_dir, '.env')
        load_dotenv(dotenv_path=dotenv_path)
        # load_dotenv()
        api_key = os.getenv("WEATHER_API_KEY")
        if not api_key:
            raise Exception("donde esta api key?")
        
        PARAMS = {'key': api_key,
            'q': self.location} #TODO: Get IP Address (seperate file?)
        r = requests.get(url = WEATHER_URL, params = PARAMS)
        data = r.json() 

        return data
    
    def current_condition(self):
        return self.weather_getter()["current"]["condition"]["text"]
        