# # https://www.weatherapi.com/docs/ = API docs

from location import Location
from weather import Weather
from wallpaper import Wallpaper

loc = Location()
print(loc.get_city())
weather = Weather(location=loc.get_city())
wallpaper = Wallpaper(weather=weather)

print(weather.current_condition())

wallpaper.set_wallpapers()



# print(data["current"]["temp_f"])
# print(data["current"]["condition"]["text"])

# # plan
# # figure out how osascript works
# # get it to change wall paper
# # link it all together


