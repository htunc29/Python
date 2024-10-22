# 1- 3 Ürün bilgisini (id,ad,fiyat) kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız
# 2- Ürün id bilgisini kullanıcıdan alıp ilgili ürün bilgisini gösterin
ürünler={

}
id=int(input("Ürün id:"))
ad=input("Ürün Adı:")
fiyat=float(input("Ürün Fiyatı:"))
ürünler[id]={
    "ad":ad,
    "fiyat":fiyat
}
print("--------------------------")
id=int(input("Ürün id:"))
ad=input("Ürün Adı:")
fiyat=float(input("Ürün Fiyatı:"))
ürünler[id]={
    "ad":ad,
    "fiyat":fiyat
}
print("--------------------------")
id=int(input("Ürün id:"))
ad=input("Ürün Adı:")
fiyat=float(input("Ürün Fiyatı:"))
ürünler[id]={
    "ad":ad,
    "fiyat":fiyat
}
print("--------------------------")



id=int(input("Bilgisini Görmek İstediğin Ürün ID:"))
print(ürünler[id])
