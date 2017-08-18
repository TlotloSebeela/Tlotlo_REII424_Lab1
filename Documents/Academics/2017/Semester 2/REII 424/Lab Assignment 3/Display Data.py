#Task 4 - Display file content to inspect content
import csv

with open("data.csv") as g:
	reader = csv.reader(g)
	for row in reader:
		print(" ".join(row))
			
