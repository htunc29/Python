# def selamlama(isim="Kullanıcı",mesaj="iyi günler",):
#     print(f"{mesaj} {isim}")
# selamlama("ali","iyi günler")
# selamlama("hüseyin","merhaba")
# selamlama("gizay")
# selamlama()

# def usAlma(taban=3,us=2):
#     return taban**us
# sonuc=usAlma(3,2)
# sonuc=usAlma()
# print(sonuc)

def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b
def cikarma(a,b):
    return a-b
def toplama(a,b):
    return a+b
def islem(a,b,fn):
    return fn(a,b)
sonuc=islem(2,56,toplama)
print(sonuc)