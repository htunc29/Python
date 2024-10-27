class Person:
    def __init__(self,name,surname,age):
        self.name=name
        self.surname=surname
        self.age=age
    def intro(self):
        print(self.name,self.surname,self.age)
class Student(Person):
    pass
class Teacher(Person):
    pass

ogrenciA=Student("Hüseyin","Tunç",21)
ogrenciB=Student("Cihan","Dertlioğlu",19)
ogrenciC=Student("Gizay","Haseken",22)    
ogrenciD=Student("Enver","Aktaş",21)
teacher=Teacher("İsmail Hakkı","Tuncel",55)

print(ogrenciA.name)
print(ogrenciB.surname)
print(ogrenciC.age)
ogrenciD.intro()
teacher.intro()

