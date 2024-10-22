def toplam():
    return 10+20
def simdi():
    import datetime
    return datetime.datetime.now().year
# print(simdi())
def yasHesapla():
    return simdi()-2003
#print(yasHesapla())
def saat():
    import datetime
    return datetime.datetime.now().hour
def selamla():
    if(saat()<12):
       return "Günaydın"
    else:
        return "Merhaba"

sonuc=selamla()+" Hüseyin"
print(sonuc)
