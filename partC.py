import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Open file
with open("activity.csv", "r") as file:
  csv_lines = file.read().split("\n")
  data = []
  for line in csv_lines[1:-1]:
    data.append(line.split(","))
"""PART C"""
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
  
def counting_nas(data):
  #Calculating the number of NAs
  total_nas = 0
  for i in data:
    if i[0] == "NA":
      total_nas += 1
  return total_nas


def fix_dataset(data):
  #We will fill in the NAs with the average steps taken on that interval on other days instead
  for i in range(len(data)):
    if data[i][0] == "NA":
      total_steps_same_interval = 0
      same_interval_counter = 0
      for j in range(len(data)):
        if data[j][0] != "NA":
          if data[j][2] == data[i][2]:
              total_steps_same_interval += int(data[j][0])
              same_interval_counter += 1
      try:
        data[i][0] = total_steps_same_interval // same_interval_counter
      except:
        data[i][0] = 0
    print(data[i])

print("NUMBER OF NAs")
print(counting_nas(data))

print("\n\nFIXING NAs")
print(fix_dataset(data))

steps_per_day = steps_per_day_func(data)

print("\n\nMEAN AND MEDIAN")
new_mean_n_median = mean_and_median(steps_per_day)
print("mean: {} \nmedian: {}".format(new_mean_n_median[0], new_mean_n_median[1]))

print("\n\nHISTOGRAM")
histogram(steps_per_day)
