import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
with open("activity.csv", "r") as file:
  csv_lines = file.read().split("\n")
  data = []
  for line in csv_lines[1:-1]:
    data.append(line.split(","))

"""PART B"""
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

ts = time_series(data)

#Printing the interval with the most steps
maximum = 0
index = 0
final_index = 0
for i in ts[1]:
  if i > maximum:
    maximum = i
    final_index = index
  index += 1
highest = ts[0][final_index]
print("interval with most steps on average: {}".format(highest))