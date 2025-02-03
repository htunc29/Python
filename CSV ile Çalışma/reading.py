from csv import DictReader
# with open("Automobile.csv") as file:
#     print(file.read()) 

with open("sportcar.csv") as file:
    csv_reader=DictReader(file)
    for p in csv_reader:
        if(p["Model"].lower().__contains__("chiron")):
            print(p["Model"])
