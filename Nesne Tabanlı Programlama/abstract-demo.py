import datetime
class Blog:
    
    def __init__(self,title,content,User):
        self.created_at=datetime.datetime.now().date()
        self.user=User
        self.title=title
        self.content=content
    def blogyaz(self):
        return f"{self.title} \n {self.content} \n {self.user.firstname} \n {self.created_at}"

class User:
    
  
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
        
    def fullname(self):
        return f"{self.firstname} {self.lastname}"


class Moderator(User):
    active_moderator=0
    @classmethod
    def display_active_moderator(cls):
        return f"şu anda aktif moderator {cls.active_moderator}"
    def __init__(self,firtname,lastname,comminity):
        super().__init__(firtname,lastname)
        self.comminity=comminity
        Moderator.active_moderator+=1


u1=User("Ali","Korkmaz")
m1=Moderator("Hüseyin","Tunç","Yazılım")
# print(isinstance(u1,User))
# print(isinstance(u1,Moderator))
# print(isinstance(m1,Moderator))
print(u1.fullname())
print(m1.fullname())
blog=Blog("Python Nedir","Python bir programlama dilidir",m1)
print(blog.blogyaz())
blog2=Blog("C# nedir","C# masaüstü ve web alanında kullanılan bir programalam dilidir",User("Mahmut","Ceylan"))
print(blog2.blogyaz())
# print(Moderator.display_active_moderator())