import pandas as pd

data = pd.read_csv('/home/asim/Desktop/ISDP/Sir Hammad/pandas_weather_task/files/f2.csv')

events = data[' Events']
events = data[events.isin(['Rain', 'Snow', 'Rain-Snow'])]['PKT'].tolist()

print(events)
