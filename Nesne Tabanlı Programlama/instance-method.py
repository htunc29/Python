class Person:
    #yapıcı method (constructor)
    def __init__(self,name,surname,year):
        #object attribute
        self.name=name
        self.surname=surname
        self.year=year
    def intro(self):
        return f"Benim adım {self.name} ve soyadım {self.surname}"
    def calculateAge(self):
        import datetime
        return datetime.datetime.now().year-self.year
    

p1=Person("Hüseyin","Tunç",2003)
print(p1.intro())
print(p1.calculateAge())