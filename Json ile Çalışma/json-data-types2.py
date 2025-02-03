data={
    "sadikturan":{
        "firstName":"Sadık",
        "lastName":"Turan"
    },
    "hüseyintunc":{
        "firsName":"Hüseyin",
        "lastName":"Tunç"
    }
}
with open("users2.json","w",encoding="utf-8") as file:
    import json
    json.dump(data,file,ensure_ascii=False,indent=2)
with open("users2.json",encoding="utf-8") as file:
    import json
    users=json.load(file)
print(users)
users.update({ "bedirhantunç": {
    "firsName": "Hüseyin",
    "lastName": "Tunç"
  }})
with open("users2.json","w",encoding="utf-8") as file:
    import json
    json.dump(data,file,ensure_ascii=False,indent=2)
