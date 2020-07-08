import pyowm
from pyowm.utils import timestamps
from datetime import timedelta, datetime
from api_key import API_KEY

owm = pyowm.OWM(API_KEY)
mgr = owm.weather_manager()
forecaster = mgr.forecast_at_place('Los Angeles, US', '3h')

# Write your code here
date1=timestamps.tomorrow(12,0)
date2=timestamps.tomorrow(8,30)
print(forecaster.will_be_foggy_at(date1))
print(forecaster.will_be_clear_at(date2))

