from matplotlib import pyplot as plt
from matplotlib import dates
from pyowm_helper import get_temperature

degree_sign= u'\N{DEGREE SIGN}'

def init_plot():
     plt.figure('PyOWM Weather', figsize=(5,4))
     plt.xlabel('Day')
     plt.ylabel(f'Temperature ({degree_sign}F)')
     plt.title('Weekly Forecast')



def plot_temperatures(days, temp_min, temp_max):
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
    

if __name__ == '__main__':
    init_plot()
    days, temp_min, temp_max = get_temperature()
    bar_min, bar_max = plot_temperatures(days, temp_min, temp_max)
    label_xaxis(days)
    #write_temperatures_on_bar_chart(bar_min, bar_max)
    
    plt.show()
