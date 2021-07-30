import csv

data = []
with open('something.csv') as file:
    csv_reader = csv.reader(file, delimiter = ',')
    for row in csv_reader:
        data.append(row)
for row in data:
    print(row[0])
    print(type(row[0]))
