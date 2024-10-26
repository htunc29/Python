import os 
result=dir(os)
result=os.name
# os.mkdir("new directory")
os.chdir('../..')

# etkin dizin öğrenme
# result=os.getcwd()
# os.makedirs("Pythonda Modüller/deneme")
result=os.path.abspath("_os.py")
result=os.path.dirname(os.path.abspath("_os.py"))
result=os.path.exists("C:/users/husey/python/pythonda modüller/_os.py")
print(result)