# x=10
# if x>5:
#     raise ValueError("x 5'ten büyük  olamaz")
def Colorize(text,color):
    if(type(color) is not str):
        raise TypeError("renk str tipinde olmalıdır")
Colorize("merhaba","red")
