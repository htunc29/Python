from csv import DictWriter
with open("product.csv","w") as file:
    headers=["name","price","category"]
    csv_writer=DictWriter(file,headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "name":"iphone",
        "price":2000,
        "category":"mobile"
    })
    