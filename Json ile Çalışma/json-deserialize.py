#serialize
import json
# with open("person.json",encoding="utf-8") as file:
#     data=json.load(file)
# print(data["hobbies"])
# print(type(data))
data="""
{
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
"""
data=json.loads(data)
print(data["hobbies"][1])
print(type(data))