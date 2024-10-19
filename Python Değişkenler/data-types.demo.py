'''
Daire alanı : πr^2
Daire çevresi : 2πr
** Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız. (r: 3.14)
'''
pi=3.14
yariCap=float(input("Yarı çapı giriniz: "))
alan=pi*yariCap**2
cevre=2*pi*yariCap
print("Dairenin alanı: ",alan)
print("Dairenin çevresi: ",cevre)

'''
Bir aracın km cinsinden gittiği yol ve tüketmiş olduğu toplam benzin miktarını alın ve 100 km'de ne kadar yakıt tüketildiğini hesaplayınız.
mil=kilometre/1.609344
'''
kilometre=float(input("Kilometre giriniz: "))
mil=kilometre/1.609344
print("Mil:",int(mil))