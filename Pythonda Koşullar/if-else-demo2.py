#Bir aracın yakıt tipine göre (benzin,dizel) belirtilen bir mesafede ne kadar
#yakıt masrafı olduğunu hesaplayan uygulamayı yapınız.
benzin=40.34
dizel=45.21


fueltype=input("What is Fuel Type your car ?(benzin/dizel):").lower()

unitfuel=float(input("How much use fuel your car in one hundred kilometer ?: "))

km=int(input("How many kilometers ? :"))

total=unitfuel*(km/100)
if(fueltype=="benzin"):
    print(f"{km} km yolda bu arac {int(total*benzin)} ₺ yakıt tüketir")
else:
    print(f"{km} km yolda bu arac {int(total*dizel)} ₺ yakıt tüketir")




