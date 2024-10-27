class User:
    activeUsers=0
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname
        User.activeUsers+=1
    def fullName(self):
        return f"{self.name} {self.surname}"
    def logout(self):
        return f"{self.fullName()} uygulamadan çıkış yaptı"
usera=User("Hüseyin","Tunç")
userb=User("Bedirhan","Tunç")
userc=User("Veli","Aslan")

print(f"Aktif kişi sayısı:{User.activeUsers}")
users=[usera,userb,userc]
for user in users:
    print(user.name)
print(usera.logout())

