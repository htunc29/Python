import random 
# value=dir(random)
# result=help(random)
result=random.random()
result=random.random()*100
result=random.uniform(1,100) #ondalıklı
print(random.randint(1,10))
liste=list(range(10))
random.shuffle(liste)
liste=range(100)
result=random.sample(liste,3)
print(result)

