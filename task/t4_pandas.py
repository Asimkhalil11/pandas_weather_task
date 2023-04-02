import pandas as pd
from datetime import datetime

data = pd.read_csv('/home/asim/Desktop/ISDP/Sir Hammad/pandas_weather_task/files/f2.csv')

events = data[' Events']
events = data[events.isin(['Thunderstorm'])]
events_date = pd.to_datetime(events['PKT'])
week_day = events_date.dt.strftime('%A').tolist()

print(week_day)

