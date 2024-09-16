import csv

with open("faviorite.csv", "r") as file:
    reader = csv.DictReader(file)           # read it as dict

    for row in reader:
        print(row)                          # print the row (dict)
        print(row["faviorite"])             # print faviorit col
        