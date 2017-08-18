#Task 1 - Import Data
import csv
filename = "data.csv"
f = open(filename,"r")

#Task 2 - Display Column Header
c = csv.reader(f)
i = next(c) 
print(i)
 
 #Task 3 - Display first couple of rows to inspect formating
for i in range(10): 
	j = next(c)
	print(j)

#Task 4 - Display file content to inspect content
with open("data.csv") as g:
		reader = csv.reader(g)
		for row in reader:
			print(" ",join(row))
			
