class Product:
    def __init__(self,name,price):
        self.name=name
        if price>=0:
            self._price=price
        else:
            raise ValueError("Ürün Fiyatı için nefatif değer ataması yapılamaz")
    def set_price(self,value):
        if value>0:
            self._price=value
    def get_price(self):
        return self._price
p=Product("İphone 12",9000)
print(p.get_price())
