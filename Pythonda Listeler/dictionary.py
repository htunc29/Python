# sehirler=['Kocaeli','İstanbul']
# plakalar=[41,34]
# print(plakalar[0],sehirler[0])
# print(plakalar[1],sehirler[1])
# sehir=input("İl Adı:")
# print(plakalar[sehirler.index(sehir)])
plakalar={
    'kocaeli':41,
    'istanbul':34
}
plakalar['rize']=53
print(plakalar['kocaeli'])
print(plakalar['istanbul'])
print(type(plakalar))
print(plakalar)
ogrenciler={
    2311081001:{
        "ad":"Hüseyin",
        "soyad":"Tunç",
        "yaş":21
        
    },
    2311081049:{
        "ad":"Gizay Gökberk",
        "soyad":"Haseken",
        "yaş":23
    }
}
print(ogrenciler[2311081001]["ad"])
print(ogrenciler[2311081049]["yaş"])