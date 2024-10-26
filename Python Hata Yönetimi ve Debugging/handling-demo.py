liste=["1","2","5a","10b","abc","10","50"]

# 1- Liste elemanları içerisindeki sayısal değerleri bulunuz
# for x in liste:
#     try:
#         sonuc=int(x)
#         print(sonuc)
#     except ValueError:
#         continue
urun={"urunAdi":"Samsung S10"}
def get(d,key):
  try:
      print(d[key])
  except KeyError:
     return None
  
print(get(urun,"fiyat"))
print(get(urun,"urunAdi"))
