'''
db={
    "users":{
        "tunchuseyin":{
            "firstName":"Hüseyin",
            "lastName":"Tunç"
        },
        "sadikturan": {
            "firstName": "Sadık",
            "lastName": "Turan"
        }
    },
    "products":{
        "1":{
            "productName":"Iphone 8",
            "price":5000,
        },
        "2":{
            "productName":"Iphone 12",
            "price":70000
        }
    }
}'''
'''
with open("db.json","w",encoding="utf-8") as file:
    import json
    json.dump(db,file,indent=4,ensure_ascii=False)
'''
with open("db.json","r",encoding="utf-8") as file:
    import json
    db=json.load(file)
print(db["users"]["tunchuseyin"]["lastName"])
db["products"].update({
     "3": {
            "productName": "Iphone 11",
            "price": 50000
        }
})
with open("db.json","w",encoding="utf-8") as file:
    import json
    json.dump(db,file,indent=4,ensure_ascii=False)