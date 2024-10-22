import random
hakSayisi=int(input("Hak Sayısı:"))
rndSayi=int(random.randint(1,100))
puan=100
sorupuan=100/hakSayisi
for i in range(0,hakSayisi):
    
    if(hakSayisi==0):
        print("Hakkın Doldu")
        break
    tahmin=int(input(f"{i+1}.Tahminin: "))
    if(tahmin==rndSayi):
        print("harikasın")
        break
    elif(tahmin>rndSayi):
        print("Aşağı İn")
        hakSayisi-=1
    else:
        print("Yukarı Çık")
        hakSayisi-=1
    puan-=sorupuan
    
print(f"Puanın {puan} Sayı {rndSayi}")
        