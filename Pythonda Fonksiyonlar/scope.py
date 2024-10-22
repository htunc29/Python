#global scope
# x='global x'

# def function():
#     #local scope
#     x='local x'
#     print(x)
# function()
# print(x)
# name="Çınar"
# def changeName(new_name):
#     name=new_name
#     print(name)
# changeName('ada')
# print(name)

name='global strings'
def greeting():
    global name
    def Hello():
        print('hello '+name)
    Hello()
greeting()
print(name)