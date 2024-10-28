with open("msg.txt",encoding="UTF-8",mode="") as file:
    print(file.read(10))
    print(file.tell())
    print(file.read(10))