import json
person={
    "firstName":"Hüseyin",
    "lastName":"Tunç",
    "hobbies":["spor","yazılım","sinema"],
    "age":21,
    "children":[
        {
            "firstName":"Çınar",
            "age":3
        }
    ]
}
print(person)
print(type(person))
# sonuc=json.dumps(person,ensure_ascii=False,indent=2)
# print(sonuc)
# print(type(sonuc))
with open("person.json","w",encoding="utf-8") as file:
    json.dump(person,file,ensure_ascii=False)