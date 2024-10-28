#1 Kullanıcıdan aldığı ürün bilgisini(ad,fiyat) urunler.txt dosyasına kayıt eden fonksiyon
# def urunEkle(ad,fiyat):
#     with open("urunler.txt","a",encoding="utf-8") as file:
#         file.write(f"\nAd:{ad} Fiyat:{fiyat}")
# for i in range(10):
#     ad=input("Ürün Adı:")
#     fiyat=input("Ürün Fiyatı:")
#     urunEkle(ad,fiyat)





#2 dosya ismi,eski kelime,yeni kelime parametrelerini alarak dosyada bir güncelleme yapan fonksiyon
def changeWord(filename,oldword,newword):
    with open(filename,"r+",encoding="utf-8")as file:
        metin=file.read()
        metin=metin.replace(oldword,newword)
    with open(filename,"w",encoding="utf-8") as file:
        file.write(metin)
filename=input("Dosya Adı:")
oldword=input("Eski Kelime:")
newword=input("Yeni Kelime")
changeWord(filename,oldword,newword)