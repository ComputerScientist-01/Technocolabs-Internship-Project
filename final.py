import os
import pytz
import pyowm
import streamlit as st
from matplotlib import dates
from tabulate import tabulate
from datetime import datetime
from matplotlib import pyplot as plt

owm=pyowm.OWM('0833f103dc7c2924da06db624f74565c')
mgr=owm.weather_manager()
degree_sign= u'\N{DEGREE SIGN}'

st.title("5 Day Weather Forecast")

st.write("### Write the name of a City and select the Temperature Unit and Graph Type from the sidebar")

place=st.text_input("NAME OF THE CITY :", "")

if place == None:
    st.write("Input a CITY!")

unit=st.selectbox("Select Temperature Unit",("Celsius","Fahrenheit"))

g_type=st.selectbox("Select Graph Type",("Line Graph","Bar Graph"))

if unit == 'Celsius':
    unit_c = 'celsius'
else:
    unit_c = 'fahrenheit'

   

def get_temperature():
    days = []
    dates = []
    temp_min = []
    temp_max = []
    forecaster = mgr.forecast_at_place(place, '3h')
    forecast=forecaster.forecast
    for weather in forecast:
        day=datetime.utcfromtimestamp(weather.reference_time())
        #day = gmt_to_eastern(weather.reference_time())
        date = day.date()
        if date not in dates:
            dates.append(date)
            temp_min.append(None)
            temp_max.append(None)
            days.append(date)
        temperature = weather.temperature(unit_c)['temp']
        if not temp_min[-1] or temperature < temp_min[-1]:
            temp_min[-1] = temperature
        if not temp_max[-1] or temperature > temp_max[-1]:
            temp_max[-1] = temperature
    return(days, temp_min, temp_max)

def init_plot():
     plt.figure('PyOWM Weather', figsize=(5,4))
     plt.xlabel('Day')
     plt.ylabel(f'Temperature ({degree_sign}F)')
     plt.title('Weekly Forecast')



def plot_temperatures(days, temp_min, temp_max):
    days = dates.date2num(days)
    bar_min = plt.bar(days-.25, temp_min, width=0.5, color='#4286f4')
    bar_max = plt.bar(days+.25, temp_max, width=0.5, color='#e58510')
    return (bar_min, bar_max)

def plot_temperatures_line(days, temp_min, temp_max):
    days = dates.date2num(days)
    bar_min = plt.plot(days, temp_min)
    bar_max = plt.plot(days, temp_max)
    return (bar_min, bar_max)

def label_xaxis(days):
    plt.xticks(days)
    axes = plt.gca()
    xaxis_format = dates.DateFormatter('%m/%d')
    axes.xaxis.set_major_formatter(xaxis_format)

def write_temperatures_on_bar_chart(bar_min, bar_max):
    axes = plt.gca()
    y_axis_max = axes.get_ylim()[1]
    label_offset = y_axis_max * .1
    # Write the temperatures on the chart
    for bar_chart in [bar_min, bar_max]:
        for index, bar in enumerate(bar_chart):
            height = bar.get_height()
            xpos = bar.get_x() + bar.get_width()/2.0
            ypos = height - label_offset
            label_text = str(int(height)) + degree_sign
            plt.text(xpos, ypos, label_text,
                 horizontalalignment='center',
                 verticalalignment='bottom',
                 color='white')

def draw_bar_chart():
    days, temp_min, temp_max = get_temperature()
    bar_min, bar_max = plot_temperatures(days, temp_min, temp_max)
    label_xaxis(days)
    write_temperatures_on_bar_chart(bar_min, bar_max)
    st.pyplot()
    st.subheader("Minimum and Maximum Temperatures")
    for i in range (0,5):
        st.write(temp_min[i],' - ',temp_max[i])

def draw_line_chart():
    days, temp_min, temp_max = get_temperature()
    bar_min, bar_max = plot_temperatures_line(days, temp_min, temp_max)
    label_xaxis(days)
    st.pyplot()
    st.subheader("Minimum and Maximum Temperatures")
    for i in range (0,5):
        st.write(temp_min[i],' - ',temp_max[i])
    

if __name__ == '__main__':
    #init_plot()
    if st.button("SUBMIT"):
        if g_type == 'Line Graph':
            draw_line_chart()
        else:
            draw_bar_chart()
        
    
    
