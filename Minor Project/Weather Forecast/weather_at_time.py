import pyowm
from pyowm.utils import timestamps
from datetime import timedelta, datetime
from api_key import API_KEY

degree_sign = u'\N{DEGREE SIGN}'

owm = pyowm.OWM(API_KEY)
mgr = owm.weather_manager()
forecaster = mgr.forecast_at_place('Los Angeles, US', '3h')

time = datetime.now() + timedelta(days=0, hours=12)
weather = forecaster.get_weather_at(time)
temperature = weather.temperature(unit='fahrenheit')['temp']
#print(f'The temperature at {time.strftime("%Y-%m-%d %H:%M:%S")} is {temperature}{degree_sign}F')

time = timestamps.tomorrow(15,0)
weather = forecaster.get_weather_at(time)
temperature = weather.temperature(unit='fahrenheit')['temp']
print(f'The temperature at {time} is {temperature}{degree_sign}F')

