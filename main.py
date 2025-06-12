# # https://www.weatherapi.com/docs/ = API docs

from location import Location
from weather import Weather
from wallpaper import Wallpaper

loc = Location()
print(loc.get_city())
weather = Weather(location=loc.get_city())
wallpaper = Wallpaper(weather=weather.current_condition())

print(weather.current_condition())
print(wallpaper.get_wallpaper())
wallpaper.set_wallpapers()




# print(data["current"]["temp_f"])
# print(data["current"]["condition"]["text"])

#TODO: Make it run every hour
#TODO: Get a reset control
#TODO: Use an API to fetch wallpapers
#TODO: how should I get the absolute file path for other people
#TODO: Bundle into Platypus


