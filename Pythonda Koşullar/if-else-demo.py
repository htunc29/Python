# 1- Girilen sayının 50-100 arasında olup olmadığını kontrol edin
number=int(input("Number:"))
if(number>=50) and (number<=100):
    print(f"{number} sayısı 50-100 arasında")
else:
    print(f"{number} sayısı 50-100 arasında değil")
# 2- Girilen bir sayının pozitif tek sayı olup olmadığını kontrol ediniz
number=int(input("Number:"))
if(number>0) and (number%2==1):
    print("Pozitif ve tek sayı")
else:
    print("Pozitif ve tek sayı değil")
# 3- Username ve parola bilgileri ile giriş kontrolü yapınız
username=input("username:")

if(username=="admin"):
    password=input("password:")
    if(password=="1234"):
        print(f"{username} welcome")
    else:
        print("Password is not correct")
else:
    print("user not found")