def displayUser(*args):
    print(type(args))
displayUser()
def displayUser(**kwargs):
   for key,value in kwargs.items():
       print(key,value)
displayUser(username="sadikturan",email="info@sadikturan.com")
def myFunc(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)
myFunc(10,20,30,40,50,60,70,username="ali",password="mahmut")