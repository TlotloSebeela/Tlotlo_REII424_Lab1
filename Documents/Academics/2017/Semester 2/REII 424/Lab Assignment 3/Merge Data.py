#Task 6 - Merge two datasheets on the Time Stamp field

import pandas as pd

a = pd.read_csv("LoadData.csv") #load 1st file
b = pd.read_csv("WeatherData.csv") #load 2nd file
merged = a.merge(b, on="TimeStamp")
merged.to_csv("merged.csv", index=False)

import csv
f2 = open("merged.csv","r")
l = csv.reader(f2) #assumed to be the which is being read
m = next(l)

print(m) #writing the read lines to the new csv file
