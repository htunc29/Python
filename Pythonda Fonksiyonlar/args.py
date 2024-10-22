liste=[10,20,30]
def toplam(sayilar):
    sonuc=0
    for i in sayilar:
        sonuc+=i
    return sonuc
# def toplam(a,b,c):
#     return a+b+c
# print(toplam(liste))
def toplam(*args):
    sonuc=0
    for i in args:
        sonuc+=i
    return sonuc
print(toplam(1,20,56,78,12))