import pandas as pd

data = pd.read_csv('/home/asim/Desktop/ISDP/Sir Hammad/pandas_weather_task/files/f1.csv')

max_min_difference = data['Max TemperatureC'] - data['Min TemperatureC']
max_min_difference_tolist = max_min_difference.tolist()

print(max_min_difference_tolist)
