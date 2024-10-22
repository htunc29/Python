# Kendisine gönderilen 2 sayıdan hangisi büyük bulan fonksiyonu yazınız.
# def myFun(a,b):
#     list=[a,b]
#     print(max(list))
# myFun(20,30)


# Kendisine gönderilen bir string bilgi içinde her karakter kaçar kez tekrarlanmış bulunuz.
# def analiz(kelime):
#     for x in kelime:
#         print(f"{x} karakterinden {str(kelime).count(x)} adet var")
# analiz("Barcelona")




# Kendisine gönderilen list, command, position ve value bilgilerine göre liste üzerinde güncelleme yapınız.
# def updateList(liste,command,position,value=None):
#     if(command=="remove" and position=="end"):
#         return liste
#     elif(command=="remove" and position=="beginning"):
#         return liste
#     elif(command=="add" and position=="end"):
#         liste.append(value)
#         return liste
#     elif(command=="add" and position=="beginning"):
#         liste.insert(0,value)
#         return liste
# sonuc=updateList([1,2,3],"add","end",4)
# sonuc=updateList([3,4,5,6,7,8],"remove","begining")
# print(sonuc)

def contains(*args):
   for renk in args:
      if(renk.find('blue')):return True
   return False
print(contains('red','blue','yellow'))