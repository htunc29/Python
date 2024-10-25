multiply=(lambda a:a**2)  
sonuc=multiply(5)
toplama=lambda a,b,c:a+b+c
sonuc=toplama(1,5,7)
tersCevir=lambda a:a[::-1]
sonuc=tersCevir("elma")

def myFunc(n):
    return lambda a:a*n
multiply2=myFunc(2)
sonuc=multiply2(10)
print(sonuc)
