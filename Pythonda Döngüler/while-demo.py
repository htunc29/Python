sayilar = [4,6,9,10,35,57,89,125,244]
# 1: sayilar listesini while ile ekrana yazdırın.
# i=0
# while i<len(sayilar):
#     print(sayilar[i])
#     i+=1

# while sayilar:
#     print(sayilar.pop())
# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları 
# ekrana yazdırın.
# bas=int(input("Başlangıç:"))
# bit=int(input("Bitis:"))
# while bas<=bit:
#     if(bas%2==1):print(bas)
#     bas+=1

# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.
# i=100
# while i>=1:
#     print(i)
#     i-=1

# 4:Kullanıcıdan alacağınız beş sayıyı ekranda sıralı bir şekilde yazdırın
list=[]
i=0
while i<5:
    sayi=int(input("Sayı:"))
    list.append(sayi)
    i+=1
list.sort()
print(list)