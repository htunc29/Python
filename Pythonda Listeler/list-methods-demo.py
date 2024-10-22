isimler=["Ada","Yiğit","Hasan","Beril"]
yaslar=[1998, 2000, 1998, 1987]

# 1- "Cenk" ismini listenin sonuna ekleyiniz.
isimler.append("Cenk")
# 2- "Sena" değerini listenin başına ekleyiniz.
isimler.insert(0,"Sena")
# 3- "Yiğit" ismini listeden siliniz.
# isimler.remove("Yiğit")
# 4- "Yiğit" isminin indexini bulunuz.
index=isimler.index('Yiğit')
print(index)
# 5-  "Beril Liste elemanı mıdır?"
if "Beril" in isimler:
    print("evet")

# 6- Liste elemanlarını ters çevirin.
isimler.reverse()
yaslar.reverse()
# 7- Liste elemanlarını alfabetik olarak sıralayınız.
isimler.sort()
yaslar.sort()
# 8- yaslar listesini büyükten küçüğe sıralayınız.
yaslar.sort()
yaslar.reverse()
# 9- str="IPhone X,IPhone XR" karakter dizisini listeye çeviriniz.
str="Iphone X,Ihone XR"
newdizi=str.split(',')
print(newdizi)
# 10- yaslar dizisinin en büyük ve en küçük elemanı nedir?
print(max(yaslar))
print(min(yaslar))
# 11- yaslar dizisinde kaç tane 1998 değeri vardır?
print(yaslar.count(1998))
# 12 - yaslar dizisinin tüm elemanlarını siliniz.
yaslar.clear()
print(yaslar)
# 13 - Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
marka1=input("1.Marka:")
marka2=input("2.Marka:")
marka3=input("3.Marka:")
markalar=[marka1,marka2,marka3]
print(markalar)