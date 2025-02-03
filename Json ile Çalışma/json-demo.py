
def urunEkle(urunAdi,fiyat,satistami,kategori):
    urun={
        "urunAdi":urunAdi,
        "fiyat":fiyat,
        "satistami":satistami,
        "kategori":kategori
    }
    import json
    with open("urunler.json","w") as file:
        json.dump(urun, file,ensure_ascii=False)
urunEkle("Iphone 12",5500,True,["Elektronik","Telefon"])        
def urunleri_getir():
    import json
    with open("urunler.json") as file:
        urun=json.load(file)
    print(urun)
urunleri_getir()