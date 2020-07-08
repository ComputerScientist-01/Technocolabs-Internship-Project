import pyowm
from api_key import API_KEY

degree_sign= u'\N{DEGREE SIGN}'

owm = pyowm.OWM(API_KEY)

# Three Hours Forecast
mgr = owm.weather_manager()
forecaster = mgr.forecast_at_place('Los Angeles, US', '3h')
forecast = forecaster.forecast
weather_list = forecast.weathers

print('Three hours forecast (Times are in GMT):')
for weather in weather_list:
    temp = weather.temperature(unit='fahrenheit')['temp']
    print(weather.reference_time('iso'), f'Temperature: {temp}{degree_sign}F')
