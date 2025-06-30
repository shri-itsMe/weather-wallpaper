# # https://www.weatherapi.com/docs/ = API docs

from location import Location
from weather import Weather
from wallpaper import Wallpaper

loc = Location()
print(loc.get_city())
weather = Weather(location=loc.get_city())
wallpaper = Wallpaper(weather=weather.current_condition())
wallpaper.capture_wallpaper()

print(weather.current_condition())
print(wallpaper.get_wallpaper())
wallpaper.set_wallpaper()

# print(wallpaper.user_default())

# if input("change back? T or F: ") == "T":
#     wallpaper.user_default()




