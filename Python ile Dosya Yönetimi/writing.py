file=open("newfile.txt","w",encoding="utf-8")
file.write("Bedirhan Tunç")
with open("newfile.txt",encoding="utf-8") as file:
    print(file.read())