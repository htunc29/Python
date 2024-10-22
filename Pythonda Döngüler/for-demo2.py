urunler = [
    {'name':'iphone 8', 'price': '4000' },
    {'name':'iphone 8 Plus', 'price': '5000' },
    {'name':'iphone X', 'price': '6000' },
    {'name':'iphone XR', 'price': '7000' },
    {'name':'iphone 11', 'price': '8000' },
    {'name':'samsung s10', 'price': '6000' },
]

# 1- Tüm ürün bilgilerini listeleyiniz.
for x in urunler:
    print(f"{x['name']} {x['price']}")
# 2- Ürünlerin fiyatları toplamı nedir ?
total=0
for x in urunler:
    total+=int(x['price'])
print(total)
# 3- Ürünlerden fiyatı en fazla 6000 olan ürünleri gösteriniz ?
for x in urunler:
    if(int(x['price'])<=6000):print(f"{x['name']} {x['price']}")
# 4- Kullanıcıdan alınan anahtar kelimeyi içeren ürünleri bulunuz.
keyword=input("Anahtar Kelime:")
for x in urunler:
    if(x["name"].find(keyword)==0):print(f"{x['name']} {x['price']}")