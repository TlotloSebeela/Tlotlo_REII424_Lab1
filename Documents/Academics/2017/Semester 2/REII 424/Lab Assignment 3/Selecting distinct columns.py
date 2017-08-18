#Author : Tlotlo Sebeela
#Task 5 - Select only column 1 , 3, 5 from data.csv file and stored in a new file name reduced.csv

import csv
fl = open("data.csv","r")
user_dict = {}
with open('reduced.csv','wb') as f:#output csv file	
	writer = csv.writer(f)
	with open('data.csv','r') as csvfile: #input csv file
		reader = csv.DictReader(csvfile, delimiter = ',')
		for row in reader:
			j = row['Time Stamp'],row['Name'],row['Load'] 
			print(j)
			
fl.close()
