import csv 

with open('winequality-red.csv') as csvfile: 
    reader = csv.reader(csvfile, delimiter=' ');
    for row in reader: 
        print(', '.join(row))
