isimler = ["Ahmet","ali","Çınar","DeNiz"]
string = "Hello 123456 World."
yillar = [1983, 1999, 2008, 1956, 1986]
dereceler = [20,5,15,-2,0,-6]

# 1- "1-100" arasındaki sayılardan 12' e tam bölünebilen sayı listesi oluşturunuz.
# sonuc=[i for i in range(1,101) if i%3==0 and i%4==0]
# print(sonuc)
# 2- isimler listesindeki her ismi küçük harfe çevirip tersten yazdınız.
# sonuc=[isim.lower()[::-1] for isim in isimler]
# print(sonuc)
# 3- verilen "string" içindeki rakamları içeren bir liste oluşturunuz.
# sonuc=[rakam for rakam in string if rakam.isdigit()]
# print(sonuc)
# 4- "yillar" dizisindeki her doğum yılı için yaş bilgisini içeren liste oluşturunuz.
# import datetime
# sonuc=[datetime.datetime.now().year-i for i in yillar]
# print(sonuc)

# 5- "dereceler" listesinde bulunan hava sıcaklık bilgisine göre eksi değer için buzlanma tehlikesi yazdırınız.
sonuc=[derece if derece>0 else f"{derece} Buzlanma Tehlikesi" for derece in dereceler]
print(sonuc)