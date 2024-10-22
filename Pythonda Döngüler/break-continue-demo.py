#1-100 arasındaki çift sayılar toplamı
i=0
total=0
while i<=100:
    i+=1
    if(i%2==1):
        continue
    total+=i
    
print(total)