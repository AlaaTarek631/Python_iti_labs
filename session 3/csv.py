import csv

Data = csv.reader(open("test.csv", "r+"))

dictionary = {}

for l in Data:
	dictionary[l[0]] = {'letter':l[1],'num':l[1]}
print(dictionary)