# Hockeyspelare
# namn     Peter Forsberg
# jersey   21 
# team     Colorado


# import os
# with open("namn.txt", "r") as f:
#     for line in f:
#         print(line.replace("\n", ""))

import json
from datetime import datetime
from os.path import exists

def default(obj):
    if isinstance(obj, datetime):
        return { '_isoformat': obj.isoformat() }
    raise TypeError('...')

def object_hook(obj):
    _isoformat = obj.get('_isoformat')
    if _isoformat is not None:
        return datetime.fromisoformat(_isoformat)
    return obj

class Player:
    Namn = ""
    Team = ""
    Jersey = ""
    LastModified = None

    @classmethod
    def create(cls,in_dict:dict):
        a = cls()
        a.__dict__ = in_dict
        return a    
listOfPlayers = []
#läsa players.json och skapa Player med dom värdena
# stoppa in i listan
if exists("players.json"):
    with open("players.json", "r") as f:
        data = json.load(f,object_hook=object_hook)
        for dic in data:
            p = Player.create(dic)
            listOfPlayers.append(p)        

  
while True:
    print("1. Skapa ny")
    print("2. Lista alla ")
    selection = input("Val:")
    if selection == "1":
        player = Player()
        player.Namn = input("Ange namn:")
        player.Jersey = int(input("Ange jersey:"))
        player.Team = input("Ange team:")
        player.LastModified = datetime.now()
        listOfPlayers.append(player)
        with open('players.json', 'w') as json_file:
            json.dump([b.__dict__ for b in listOfPlayers], json_file,default=default)        
    if selection == "2":
        for p in listOfPlayers:
            print(f"{p.Namn} Nummer: {p.Jersey}  {p.Team}")