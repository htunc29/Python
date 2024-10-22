# 1- Çarpım tablosu hazırlayınız.
# for i in range(1,10):
#     for j in range(1,11):
#         print(f"{i} x {j} = {i*j}")
#     print("--------------------")
# 2- Girilen bir sayının asal olup olmadığını kontrol ediniz..
#    Asal Sayı 1 ve kendisi hariç tam böleni olmayan sayılara denir. 
number=int(input("sayı:"))
asalMı=True
if(number==1):asalMı=True
for i in range(2,number):
   
    if(number%i==0):
        asalMı=False
        break
    else:asalMı=True
if asalMı:print("Asal")
else:print("Asal Değil")

