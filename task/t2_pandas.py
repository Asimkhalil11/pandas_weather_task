import pandas as pd

data = pd.read_csv('/home/asim/Desktop/ISDP/Sir Hammad/pandas_weather_task/files/f1.csv')

max_min_difference = data['Max TemperatureC'] - data['Min TemperatureC']
average = max_min_difference/2
average_tolist = average.tolist()
print(average_tolist)

