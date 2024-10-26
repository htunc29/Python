from db import urunler
import random
def urunEkle(urunAd,fiyat):
    urunler.append({"id":random.randint(1,100),"urunAd":urunAd,"fiyat":fiyat})
    return "Eklendi"
def urunGuncelle(id,urunAd,fiyat):
    for urun in urunler:
        if(urun["id"]==id):
            urun["urunAd"]=urunAd
            urun["fiyat"]=fiyat
            break
    print("Güncellendi")
def urunListele():
    return urunler