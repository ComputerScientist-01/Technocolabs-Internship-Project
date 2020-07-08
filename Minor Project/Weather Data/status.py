import pyowm
from api_key import API_KEY

owm = pyowm.OWM(API_KEY)
mgr = owm.weather_manager()
obs = mgr.weather_at_place('Seattle, US')
weather = obs.weather
dstatus = weather.detailed_status
status=weather.status
print(f"Today's weather: {status}")
print(f"Today's weather: {dstatus}")
