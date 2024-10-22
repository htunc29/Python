def selamla(isim):
    return f"Merhaba,{isim}"
selamla("Hüseyin")
sonuc=selamla("Hüseyin")
print(sonuc)
def toplam(a,b):
    return a+b
sonuc=toplam(210,20)

def yasHesapla(dogumYili):
    return 2024-dogumYili
sonuc=yasHesapla(2003)
sonuc=yasHesapla(2006)

def emekliligeKacYilKaldi(dogumYili,isim):
    yas=yasHesapla(dogumYili)
    kalanSure=65-yas
    if(kalanSure>0):print(f"{isim}, emekliliğinize {kalanSure} yıl kaldı")
    else:
        print(f"{isim},zaten  {abs(kalanSure)} yıl önce emekli oldunuz")

emekliligeKacYilKaldi(1956,"Hüseyin")