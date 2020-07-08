import pytz
from datetime import datetime

def gmt_to_eastern(unix_gmt):
    eastern = pytz.timezone('US/Eastern')
    gmt = pytz.timezone('GMT')
    date = datetime.utcfromtimestamp(unix_gmt)
    date = gmt.localize(date)
    eastern_time = date.astimezone(eastern)
    return eastern_time


if __name__ == '__main__':
    for timezone in pytz.all_timezones:
        print(timezone)
