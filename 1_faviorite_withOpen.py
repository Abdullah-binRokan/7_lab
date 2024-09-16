import csv

with open("faviorite.csv", "r") as file:    # with open closes the file once finished
    reader = csv.reader(file)
    next(reader)            # exclude the header row

    for row in reader:
        print(row[2])