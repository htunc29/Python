msg="Merhaba repoma hoşgeldiniz.Ben Hüseyin Tunç"
# sonuc=msg.upper() her harf büyük olur
# sonuc=msg.lower() her harf küçük olur
# sonuc=msg.title() her kelimenin ilk harfi büyük olur
# sonuc=msg.capitalize() # sadece ilk harf büyük olur
# sonuc=msg.islower() # tüm harfler küçük mü
# sonuc=msg.endswith("Tunç") #sonunda Tunç var mı
# sonuc=msg.startswith("Merhaba") #başında Merhaba var mı
# sonuc=msg.strip() # boşluklara göre ayırır
# sonuc=msg.split() # boşluklara göre ayırır
# for i in sonuc:
#     print(i)
# sonuc="-".join(msg)
# index=msg.find("Hüseyin") # Hüseyin kelimesinin başlangıç indexini verir
sonuc=msg.replace(' ','-') # boşlukları - ile değiştirir
print(sonuc)