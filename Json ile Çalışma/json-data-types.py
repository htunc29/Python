user={
    "username":"tnc29",
    "firstname":"Hüseyin",
    "lastname":"Tunç"
}
import json
with open("users.json") as file:
    users=json.load(file)
data=users.append(user)

import json
with open("users.json","w") as file:
    json.dump(users,file,ensure_ascii=False,indent=2)