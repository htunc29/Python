opelObj={
    "marka":"Opel",
    "model":"Corsa",
    "yil":2020
}

sonuc=opelObj["marka"]
print(sonuc)

for x in opelObj:
    print(x)
for x in opelObj:
    print(opelObj[x])
for x in opelObj.values():
    print(x)
for x,y in opelObj.items():
    print(f"{x}:{y}")
sonuc="marka" in opelObj
print(sonuc)
print(opelObj)
obj=opelObj.copy()
obj["marka"]="Mazda"
opelObj.update({
    'marka':'BMW'
})
print(obj)
print(opelObj)