import pyowm
from api_key import API_KEY

owm = pyowm.OWM(API_KEY)
mgr = owm.weather_manager()
obs = mgr.weather_at_zip_code('98101', 'US')
weather = obs.weather
temperature = weather.temperature(unit='fahrenheit')['temp']

print(f'The temperature is {temperature} degrees Fahrenheit.')
