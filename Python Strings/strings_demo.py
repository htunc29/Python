website="http://www.vekaletim.com"
kursAdi="Python Dersleri: Baştan Sona Python Programlama"
print(len(kursAdi)) #karakter sayısı
print(website[7:10]) #7 ile 10 arası Der
print(website[-4:])
print(website[:15])
print(website[-15:])
print(website[::-1])
print(website.replace("w","W"))

name,surname,age,job="Hüseyin","Tunç",21,"Öğrenci"
print(f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}.")