phones=["Samsung S5","Samsung S6","Samsung S7","Samsung S8"]
#Liste kaç elemanlıdır
print(len(phones))
#listenin ilk ve son elemanı nedir
print(phones[0],phones[-1])
#samsung s5 değerini "Samsung S9" olarak değiştir
phones[0]="Samsung S9"
#listenin -3 indeksindeki değer nedir
print(phones[-3])
#listenin ilk 2 elemanı
print(phones[:2])
#listenin son elemanı silme
phones.remove(phones[-1])
#listeye ihhone 6s ve iphone 7 ekleyiniz
phones.append("Iphone 6s")
phones.append("Iphone 7")
print(phones)
#liste elemanlarını tersten yazdır
phones.reverse()
print(phones)