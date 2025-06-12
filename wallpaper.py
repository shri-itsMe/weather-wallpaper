#Set up wallpaper changin with osscript or apple script
import subprocess
import os
import json

class Wallpaper:
    def __init__(self, weather):
        self.weather = weather
        print("Init, weather = " + str(self.weather))

    def capture_wallpaper(self):
        
        #Get file of wallpaper
        script = f'''
            tell application "System Events"
                get picture of current desktop
            end tell
        '''
        default_wallpaper = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
        #save the absolute path for the wallpaper
        config_path = os.path.abspath("./assets/config.json")
        #save the abd path in a dict
        data = {"user_wallpaper": default_wallpaper.stdout.strip()}

        #put all of that in a json
        with open(config_path, "w") as f:
            json.dump(data, f, indent=2)
        
        return True

    def get_wallpaper(self):
        print("Running find_wallpaper, weather = " + str(self.weather))
        if self.weather == "Sunny":
            wallpaper = "Sunny"
    
        elif self.weather == "Partly cloudy":
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
                set picture of current desktop to "/Users/shriya/weather-wallpaper/assets/{asset_name}.png"
            end tell
        '''

        subprocess.run(['osascript', '-e', script])
    
    def test_set_wallpapers(self):
        return str(self.get_wallpaper())
    
    def user_default(self):

        assets_folder = os.path.join(os.path.dirname(__file__), "assets")
        config_path = os.path.join(assets_folder, "config.json")

        with open(config_path) as default_wp_file:
            parsed_json = json.load(default_wp_file)
        default_wp_path = parsed_json["user_wallpaper"]
        print(default_wp_path)


        script = f'''
            tell application "System Events"
                set picture of current desktop to "{default_wp_path}"
            end tell
        '''
        subprocess.run(['osascript', '-e', script])


        return default_wp_path
