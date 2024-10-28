import csv
# with open("Automobile.csv") as file:
#     print(file.read()) 

with open("Automobile.csv") as file:
    csv_reader=csv.reader(file)
    for p in csv_reader:
        print(p)