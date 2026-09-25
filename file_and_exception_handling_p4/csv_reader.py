import csv
with open("emp.csv","r") as file:
    reader=csv.reader(file)

    for row in reader:
        print(row)