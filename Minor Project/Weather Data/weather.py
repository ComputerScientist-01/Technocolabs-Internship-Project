import pyowm
from api_key import API_KEY

owm = pyowm.OWM(API_KEY)
mgr = owm.weather_manager()
obs = mgr.weather_at_place('San Francisco, US')
weather = obs.weather
temperature = weather.temperature(unit='celsius')['temp']

print(f'The temperature in San Francisco, California is {temperature} degrees Celsius.')
