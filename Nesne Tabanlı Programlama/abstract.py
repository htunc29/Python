class Person:
    def __init__(self,name,surname,age):
        self.name=name
        self.surname=surname
        self.age=age
    def intro(self):
        print(self.name,self.surname,self.age)
class Student(Person):
    def __init__(self,name,surname,age,number):
        super().__init__(name,surname,age)
        self.number=number
        print("Student nesnesi üretildi")
    def study(self):
        print(f"{self.number} numaralı öğrenci ders çalışıyor")
    def intro(self):
        print(self.name,self.surname,self.age)
class Teacher(Person):
    def __init__(self,name,surname,age,branch):
        super().__init__(name,surname,age)
        self.branch=branch
        print("Teacher nesnesi üretildi")
    def teach(self):
        print(f"{self.name} hocası {self.branch} dersi veriyor")

ogrenciA=Student("Hüseyin","Tunç",21,200)
ogrenciB=Student("Cihan","Dertlioğlu",19,32)
ogrenciC=Student("Gizay","Haseken",22,3123)    
ogrenciD=Student("Enver","Aktaş",21,131)
teacher=Teacher("İsmail Hakkı","Tuncel",55,"Görsel Programlama")
ogrenciA.study()
teacher.teach()
print(ogrenciA.name)
print(ogrenciB.surname)
print(ogrenciC.age)
ogrenciD.intro()
teacher.intro()
ogrenciA.intro()

