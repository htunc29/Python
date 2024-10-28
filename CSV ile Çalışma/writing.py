from csv import writer,reader

# with open("cars.csv","w") as file:
#     csv_writer=writer(file)
#     csv_writer.writerow(["Marka","Model"])
#     csv_writer.writerow(["Toyata","Yaris"])
#     csv_writer.writerow(["Toyata","Coralla"])

# with open("Cars.csv","w",encoding="utf-8",newline="") as file:
#     csv_writer=writer(file)
#     csv_writer.writerows([["Marka","Model"],["Mazda","323"],["Bmw","M5 Competition"]])

with open("Automobile.csv") as file:
    csv_reader=reader(file)
    with open("new-products.csv","w") as file:
        csv_writer=writer(file)
        for car in csv_reader:
            csv_writer.writerow([p.upper() for p in car])