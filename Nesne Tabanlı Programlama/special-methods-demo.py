class NewDict(dict):
    def __repr__(self):
        print('repr metotundan mesaj var.')
        return super().__repr__()
    def __missing__(self,key):
        print("Olmayan bir key bilgisi")


data=NewDict({"firtname":"Hüseyin","lastname":"Tunç"})
data["firtname"]