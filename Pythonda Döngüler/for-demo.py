sayilar=[1,5,15,35,57,72]

# 1-sayılar listesindeki her bir elemanı yazdırın
# for x in sayilar:
#     print(x)
# 2-sayılar listesindeki hangi sayılar 5 in katıdır
# for x in sayilar:
#     if(x%5==0):print(x)
# 3-sayilar listesinde sayıların toplamı kaçtır
# print(sum(sayilar))
# 4-sayılar listesinde çift sayıların karesini alınız
# for x in sayilar:
#     if(x%2==0) : print(x**2)
urunler=["iphone 8","iphone X","iphone XR","samsung s10"]

# 5-urunler listesindeki tüm ürünlerin 2.karakterlerini ekrana yazdırın.
# for x in urunler:
#     print(x[1])
# 6-urunler listesinde içinde iphone geçen kaç ürün vardır
count=0
for x in urunler:
    if x.find("iphone")==0:count+=1
print(count)
