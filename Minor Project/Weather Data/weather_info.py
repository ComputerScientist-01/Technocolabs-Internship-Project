import pyowm
from api_key import API_KEY

owm = pyowm.OWM(API_KEY)
mgr = owm.weather_manager()
obs = mgr.weather_at_place('Los Angeles, US')
weather = obs.weather

clouds = weather.clouds
winds = weather.wind('miles_hour')['speed']
#print(f'The current cloud coverage for Los Angeles, California is {clouds}%')
print(f'The current wind speed for Los Angeles, California is {winds}mph')
