
players={

}
id=int(input("ID:"))
name=input("Player Name:")
yearOfBirth=input("Player yearOfBirth:")
currentTeam=input()
history=input("Oynadığı Takımlar(Virgül ile ayırınız):")

players[id]={
    "name":name,
    "yearOfBirth":yearOfBirth,
    "currentTeam":currentTeam,
    "history":history.split(',')
}
print("-----------------")
id=int(input("ID:"))
name=input("Player Name:")
yearOfBirth=input("Player yearOfBirth:")
currentTeam=input("Mevcut Takım:")
history=input("Oynadığı Takımlar(Virgül ile ayırınız):")

players[id]={
    "name":name,
    "yearOfBirth":yearOfBirth,
    "currentTeam":currentTeam,
    "history":history.split(',')
}
print("-----------------")
print(players)
id=input("ID")
print(players[id])