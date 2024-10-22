#    Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#    ** ürün sayısını kullanıcıya sorun.
#    ** dictionary listesi yapısı (urunAdi, fiyat) şeklinde olsun.
#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.
urunler=[]
urunSayisi=int(input("Ürün Sayısı:"))
i=0
while i<=urunSayisi:
    urunAd=input("Ürün Adı:")
    urunFiyat=input("Ürün Fiyatı:")
    urunler.append({"name":urunAd,"price":urunFiyat})
    i+=1
print(urunler)