import subprocess
import os
import json
import sys

class Wallpaper:
    def __init__(self, weather):
        self.weather = weather
        print("Init, weather = " + str(self.weather))

    def get_resource_path(self, relative_path):
        """Get the path to a resource, works for both development and bundled app"""
        try:
            # py2app path
            base_path = os.environ['RESOURCEPATH']
        except KeyError:
            # Development path
            base_path = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base_path, relative_path)

    def capture_wallpaper(self):
        #Get file of wallpaper
        script = f'''
            tell application "System Events"
                get picture of current desktop
            end tell
        '''
        default_wallpaper = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
        
        # Use resource path for config.json
        assets_folder = self.get_resource_path("assets")
        if not os.path.exists(assets_folder):
            os.makedirs(assets_folder)
            
        config_path = os.path.join(assets_folder, "config.json")
        
        #save the absolute path in a dict
        data = {"user_wallpaper": default_wallpaper.stdout.strip()}
    
        if not os.path.exists(config_path):
            #put all of that in a json
            with open(config_path, "w") as f:
                json.dump(data, f, indent=2)
        
        return True

    def get_wallpaper(self):
        print("Running find_wallpaper, weather = " + str(self.weather))
        weather_lower = self.weather.lower()
        
        if "sunny" in weather_lower or "clear" in weather_lower:
            wallpaper = "Sunny"
        elif "partly cloudy" in weather_lower or "partial" in weather_lower:
            wallpaper = "Partly_Cloudy"
        elif "rain" in weather_lower or "drizzle" in weather_lower or "shower" in weather_lower:
            wallpaper = "Rainy"
        elif "overcast" in weather_lower or "cloudy" in weather_lower:
            wallpaper = "Overcast"
        else:
            # Default fallback
            wallpaper = "Overcast"
            print(f"Unknown weather condition: {self.weather}, using default: Overcast")
        
        return wallpaper

    def set_wallpaper(self):
        asset_name = str(self.get_wallpaper())
        
        # Use resource path for assets
        assets_folder = self.get_resource_path("assets")
        new_wp_path = os.path.join(assets_folder, f"{asset_name}.png")
        
        # Check if file exists
        if not os.path.exists(new_wp_path):
            print(f"Wallpaper file not found: {new_wp_path}")
            return False
            
        print("New Wallpaper Path: " + str(new_wp_path))
        script = f'''
            tell application "System Events"
                set picture of current desktop to "{new_wp_path}"
            end tell
        '''
        
        result = subprocess.run(['osascript', '-e', script])
        return result.returncode == 0
    
    def test_set_wallpaper(self):
        return str(self.get_wallpaper())
    
    def user_default(self):
        assets_folder = self.get_resource_path("assets")
        config_path = os.path.join(assets_folder, "config.json")

        if not os.path.exists(config_path):
            print(f"Config file not found: {config_path}")
            return None

        try:
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
        except Exception as e:
            print(f"Error restoring default wallpaper: {e}")
            return None