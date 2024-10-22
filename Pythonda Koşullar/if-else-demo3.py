'''
1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme
 durumunu kontrol ediniz
''' 
# name=input("Name:")
# age=int(input("Age:"))
# educationLevel=input("Education Level (İlkokul/Ortaokul/Lise/Üniversite):").lower()

# if(age>=18) and ((educationLevel=="üniversite") or (educationLevel=="lise")):
#     print(f"{name} ehliyet alabilirsin")
# else:
#     print(f"{name} ehliyet alamazsın")

'''
2- Öğrencinin vize ve final notlarını kaldı ise büt notuna göre 
harf notunu, ortalamasını ve kaldı geçti durumunu  yazdırınız
'''
# harfnot=""
# vize=int(input("Vize:"))
# final=int(input("Final:"))

# ortalama=vize*0.4+final*0.6
# if(ortalama<50) or (final<45):
#     butunleme=int(input("Bütünleme:"))
#     final=butunleme
#     ortalama=vize*0.4+final*0.6
# if(ortalama>=81) and (ortalama<=100):
#         harfnot="AA"
# if(ortalama>=76) and (ortalama<81):
#         harfnot="BA"
# if(ortalama>=70) and (ortalama<76):
#         harfnot="BB"
# if(ortalama>=60) and (ortalama<70):
#         harfnot="CB"
# if(ortalama>=50) and (ortalama<60):
#         harfnot="CC"
# if(ortalama>=45) and (ortalama<50):
#         harfnot="DC"
# if(ortalama>=40) and (ortalama<45):
#         harfnot="DD"
# if(ortalama>=30) and (ortalama<40):
#         harfnot="FD"
# if(ortalama>=0) and (ortalama<30):
#         harfnot="FF"
# print(f"Ortalama:{ortalama} Harf Notu:{harfnot}")
   

'''
3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki
bilgilere göre hesaplayınız.
1.Bakım=>1.Yıl
2.Bakım=>2.Yıl
2.Bakım=>3.Yıl
'''
import datetime
simdi=datetime.datetime.now()
tarih=input('Trafiğe Çıkış Tarihi(19/10/2024):')
tarih=tarih.split('/')
trafikCikisTarih=datetime.datetime(int(tarih[2]),int(tarih[1]),int(tarih[0]))
fark=simdi-trafikCikisTarih
gun=fark.days
if(gun<=365):
    print("1.Servis Bakımı")
elif(gun>=365) and (gun<=365*2):
    print("2.Servis Bakımı")
else:
    print("3.Servis Bakımı")
