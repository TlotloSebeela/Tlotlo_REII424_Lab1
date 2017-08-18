#Task 1 - Import Data
import csv
filename = "merged.csv"
f = open(filename,"r")

#Task 2 - Display Column Header
c = csv.reader(f)
i = next(c) 
print(i)
 
 #Task 3 - Display first couple of rows to inspect formating
for i in range(10): 
	j = next(c)
	print(j)

