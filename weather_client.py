import requests
import json

# returns requested weather information at a given latitude and longitude
# features is a list of extra features (other than the standard alert/hourly temperature info)
# converts date/time information to local timezone
# API key is for the One Call OpenWeather API
# https://openweathermap.org/api/one-call-api
def get_weather_info(api_key, lat, lon, features):
    
    units = 'imperial'
    url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={api_key}&units={units}'
    
    url_text = requests.get(url).text
    
    weather_dict = json.loads(url_text)
    ret_dict = {}
    ret_dict['hourly'] = weather_dict['hourly']
    ret_dict['alerts'] = weather_dict['alerts']
    
    for feat in features:
        if feat in weather_dict:
            ret_dict[feat] = weather_dict[feat]
    
    return ret_dict

robbie_api_key = '8c04e1181281c54bd2d8e1d2fa88d1b4'
lat = 43.819540
lon = -69.665020

# weather info for Southport, Maine
weather = get_weather_info(robbie_api_key, lat, lon, features=[])
print(weather)