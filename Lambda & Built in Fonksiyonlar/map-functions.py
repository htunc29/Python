sayilar=[1,-2,5,7,9]
kareler=[]
kisiler=[
    {"ad":"Hüseyin","soyad":"Tunç"}
]
def KareAl(sayi):
    return sayi**2
sonuc=list(map(lambda sayi:sayi**2,sayilar))
sonuc=list(map(abs,sayilar))
sonuc=list(map(lambda x:x["ad"],kisiler))
print(sonuc)