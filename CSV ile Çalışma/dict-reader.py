from csv import DictReader

with open("Automobile.csv",) as file:
    csv_reader=DictReader(file)
    for row in csv_reader:
        if(row["name"].__contains__("mazda")):
            print(row["name"])