import pyowm
import pytz
from datetime import datetime
from api_key import API_KEY

owm = pyowm.OWM(API_KEY)
mgr = owm.weather_manager()
obs = mgr.weather_at_place('Boston, US')
weather = obs.weather

print(weather.sunrise_time(timeformat='iso'))
print(weather.sunset_time(timeformat='iso'))
