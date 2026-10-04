import csv

with open('acc.csv', 'r') as f:
    data = csv.reader(f)
    for d in data:
        print(d)