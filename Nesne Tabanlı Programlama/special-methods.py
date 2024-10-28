liste=[1,2,3]
print(len(liste))
s="Hello World"
print(len(s))
class Film:
    def __init__(self,baslik,yonetmen,sure):
        self.baslik=baslik
        self.yonetmen=yonetmen
        self.sure=sure
    def __str__(self):
        return f"{self.baslik},{self.yonetmen} tarafından yönetildi"
    def __repr__(self):
        pass
    def __len__(self):
        return self.sure
        
f=Film("film adi","yonetmen",120)
# print(len(f))
print(str(f))
print(len(f))