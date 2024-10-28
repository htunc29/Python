
with open("markalar.txt","r+",encoding="utf-8") as file:
    markalar=file.readlines()
    markalar.insert(2,"3-Renault\n")
    file.seek(0)
    for marka in markalar:
        file.write(marka)
