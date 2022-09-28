import csv
with open("airtravel.csv","r") as csv_file:
    csvFile = csv.reader(csv_file)
    for line in csvFile:
        print(line)