import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""PART A"""
#Open file
with open("activity.csv", "r") as file:
  csv_lines = file.read().split("\n")
  data = []
  for line in csv_lines[1:-1]:
    data.append(line.split(","))

def steps_per_day_func(data):
  #Finding the total steps per day
  for i in data:
    current_day = ""
    total = 0
    counter = 0
    total_per_day = []
    for i in data:
      if i[1] != current_day:
        total_per_day.append([current_day, total])
        current_day = i[1]
        total = 0
      if i[0] != "NA":
        total += int(i[0])
    total_per_day = total_per_day[1:]
    return total_per_day

def mean_and_median(steps_per_day):
  #Mean and Median
  total_steps = 0
  steps_list = []
  for i in steps_per_day:
    total_steps += i[1]
  mean = total_steps / len(steps_per_day)
  median = sorted(steps_per_day, key = lambda x:x[1])[len(steps_per_day) // 2]
  return mean, median[1]

def histogram(steps_per_day):
  #Histogram
  day = []
  total_steps = []
  for steps in steps_per_day:
    day.append(steps[0])
    total_steps.append(steps[1])

  histogram = pd.DataFrame({
      'days': day, 
      'total steps': total_steps
  })
  draw = histogram.hist()
  

print("TOTAL STEPS PER DAY")
steps_per_day = steps_per_day_func(data)
for lists in steps_per_day:
  print("Total steps on {}: {}".format(lists[0], lists[1]))

print("\n\nMEAN AND MEDIAN")
mean_n_median = mean_and_median(steps_per_day)
print("mean: {} \nmedian: {}".format(mean_n_median[0], mean_n_median[1]))

print("\n\nHISTOGRAM")
histogram(steps_per_day)