#Set up wallpaper changin with osscript or apple script
import subprocess

class Wallpaper:
    def __init__(self, weather):
        self.weather = weather
        print("Init, weather = " + str(self.weather))

    def get_wallpaper(self):
        print("Running find_wallpaper, weather = " + str(self.weather))
        if self.weather == "Sunny":
            wallpaper = "Sunny"
    
        elif self.weather == "Partly Cloudy":
            wallpaper = "Partly_Cloudy"
    
        elif self.weather == "Rainy":
            wallpaper = "Rainy"
        
        elif self.weather == "Overcast":
            wallpaper = "Overcast"

        else:
            wallpaper = "wallpaper getter = ERROR"
        
        return wallpaper
    

    
    def set_wallpapers(self):
        asset_name = str(self.get_wallpaper())

        #    tell application "System Events"
        #         set desktopCount to count of desktops
        #         display dialog desktopCount
        #     end tell
        script = f'''
            tell application "System Events"
                set picture of every desktop to "/Users/shriya/weather-wallpaper/assets/{asset_name}.png"
            end tell
        '''

        subprocess.run(['osascript', '-e', script])
    
    def test_set_wallpapers(self):
        return str(self.get_wallpaper())

