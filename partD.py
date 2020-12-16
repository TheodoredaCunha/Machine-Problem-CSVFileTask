import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from datetime import date
import calendar

#Open file
with open("activity.csv", "r") as file:
  csv_lines = file.read().split("\n")
  data = []
  for line in csv_lines[1:-1]:
    data.append(line.split(","))

def time_series(data):
  #Time Series
  intervals = []
  example_date = data[0][1]
  for i in data:
    if i[1] == example_date:
      intervals.append(i[2])

  average = []
  for interval in intervals:
    total = 0
    counter = 0
    for i in data:
      if i[2] == interval:
        if i[0] != "NA":
          total += int(i[0])
          counter += 1
    average.append(total/counter)

  plt.plot(intervals, average)
  return [intervals, average]

def add_day(data):
  for i in range(len(data)):
    uncleaned_date = data[i][1][1:-1]
    splitted_date = uncleaned_date.split("-")
    my_date = datetime.date(int(splitted_date[0]), int(splitted_date[1]), int(splitted_date[2])) 
    my_day = my_date.strftime("%w")
    if my_day == 6 or my_day == 0:
      data[i].append("weekend")
    else:
      data[i].append("weekday")

add_day(data)

print("NEW TIME SERIES PLOT")
new_ts = time_series(data)