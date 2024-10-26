yaslar=[5,12,18,24,45]

def yetiskinmi(x):
    if x>18:
        return True
    else:
        return False
sonuc =list(filter(yetiskinmi,yaslar))
sonuc=list(filter(lambda a:a>18,yaslar))
print(sonuc)