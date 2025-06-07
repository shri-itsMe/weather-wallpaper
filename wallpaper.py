#Set up wallpaper changin with osscript or apple script
import subprocess

class Wallpaper:
    def __init__(self, weather):
        self.weather = weather

    def find_wallpaper(self):
        print("Running find_wallpaper, weather = " + str(self.weather))
        if self.weather == "Sunny":
            wallpaper = "Sunny"
    
        elif self.weather == "Partly Cloudy":
            wallpaper = "Partly_Cloudy"
    
        else:
            wallpaper == "Rainy"
        
        return wallpaper
    

    
    def set_wallpapers(self):
        asset_name = str(self.find_wallpaper())

        script = '''
            tell application "System Events"
                set desktopCount to count of desktops
                display dialog desktopCount
            end tell

            tell application "System Events"
                set picture of every desktop to "/Users/shriya/weather-wallpaper/assets/{asset_name}.png"
            end tell
        '''

        subprocess.run(['osascript', '-e', script])

