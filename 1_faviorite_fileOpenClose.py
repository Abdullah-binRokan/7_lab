import csv

file = open("faviorite.csv", "r")   # open the file
reader = csv.reader(file)               # read using csv Lib
next(reader)                        # exclude the first line (the header)

for row in reader:
    print(row[2])

file.close()                        # closing the file 
