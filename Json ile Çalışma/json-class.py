class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
p1=Product("Samsung S10",5000)
p2=Product("Samsung S11",6000)
products=[
    p1.__dict__,
    p2.__dict__
]
import json
with open('urunler.json',"w",encoding="utf-8") as f:
    json.dump(products,f,ensure_ascii=False)