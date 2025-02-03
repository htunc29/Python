# 1- Girilen sayının 0-50 arasında olup olmadığını kontrol edin
sayi=int(input("Sayı Giriniz:"))
if 0<sayi<50:
    print(f"{sayi} 0 ile 50 arasında")
else:print(f"{sayi} 0 ile 50 arasında değil")
# 2- Girilen sayının pozitif çift sayı olup olmadığını kontrol edin
sayi=int(input("Sayı Giriniz:"))
if sayi>0 and sayi%2==0:
    print(f"{sayi} Pozitif çift sayı")
else:print(f"{sayi} pozitif çift sayı değil")
# 3- Email ve parola bilgileri ile giriş kontrolü yapınız (email: email@gmail.com şifre:123)
email=input("email:")
sifre=input("sifre:")
if email=="email@gmail.com" and sifre=="123":
    print("Giriş başarılı")
else:
    print("Kullanıcı bulunamadı")
# 4- Girilen 3 sayıdan en büyüğünü bulunuz
sayilar=[]
for i in range(0,3):
    sayi=int(input("Sayi:"))
    sayilar.append(sayi)
print(f"En büyük sayı: {max(sayilar)}")

# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın
vize=float(input("Vize:"))*0.6
final=float(input("Final:"))*0.4
ortalama=vize+final
sonuc=""
if(ortalama>=50):
   sonuc="geçti"
else:
   sonuc="kaldı"
print(f"ortalama:{ortalama} sonuç:{sonuc}")
# 6- Hava durumuna göre etkinlik önerin:
#    Sıcaklık 30+ ise yüzme
#    Sıcaklık 20-30 arası ise piknik
#    Sıcaklık 5-20 arası ise sinema
#    Sıcaklık 5 altı ise kayak öner
hava=float(input("Hava Durumu:"))
if hava>30:
    aktivite="yüzme"
elif hava>20:
    aktivite="piknik"
elif hava>5:
    aktivite="sinema"
else:
    aktivite="kayak"
print(aktivite)