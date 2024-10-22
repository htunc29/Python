# 1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız. 
# def tekrarla(kelime,kackez):
#     for i in range(kackez):
#         print(kelime)
# tekrarla("ali",3)


# 2- Dikdörgenin alan ve çevresini hesaplayan fonksiyonu yazınız.
# def hesapla(a,b):
#     cevre=2*(a+b)
#     alan=a*b
#     print(f"Alan:{alan} Çevre:{cevre}")
# hesapla(12,34)



# 3- Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random modülü)
# def yaziTuraAt():
#     import random
#     choice=["yazı","tura"]
#     print(random.choice(choice))
# yaziTuraAt()




# 3- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.

def asalbul(sayi1,sayi2):
     
     for sayi in range(sayi1,sayi2+1):
          if(sayi>1):
               for i in range(2,sayi):
                    if(sayi%i==0):
                         break
               else:
                    print(sayi)
           



print(asalbul(20,40))




# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.
def tamBolenleriBul(sayı):
     tamBolenler=[i for i in range(1,sayı) if sayı%i==0]
    #  for i in range(1,sayı):
    #       if(sayı%i==0) : tamBolenler.append(i)
    #       else:continue
     return tamBolenler
print(tamBolenleriBul(20))