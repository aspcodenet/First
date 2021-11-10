# Hockeyspelare
# namn     Peter Forsberg
# jersey   21 
# team     Colorado

from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:hejsan123@localhost/testdatabasen'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databasen.db'
db = SQLAlchemy(app)

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Namn = db.Column(db.String(80), unique=False, nullable=False)
    Team = db.Column(db.String(30), unique=False, nullable=False)
    Jersey = db.Column(db.Integer, unique=False, nullable=False)
    #LastModified = db.Column(db, unique=False, nullable=False)

class Referee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Namn = db.Column(db.String(80), unique=False, nullable=False)
    Rating = db.Column(db.Integer, primary_key=True)
    Country  = db.Column(db.String(40), unique=False, nullable=False)

def getSafeInt(text:str, minvalue:int, maxvalue:int)->int:
    while True:
        try:        
            tal = int(input(text))
            if tal >= minvalue and tal <= maxvalue:
                return tal 
            print(f"Ange ett tal mellan {minvalue} and {maxvalue}")
        except:
            print("Ange ett tal tack")

def getText(text:str, minlength:int, maxlength:int)->str:
    while True:
        txt = input(text)
        if len(txt) <= maxlength and len(txt) >= minlength:
            return txt
        print(f"Minst:{minlength} tecken och max:{maxlength} tecken tack")



db.create_all()


  
while True:
    print("1. Skapa ny spelare")
    print("2. Lista alla spelarfe")
    print("4. Sök spelare")
    print("3. Edit spelare")
    print("5. Delete spelare")
    selection = input("Val:")
    if selection == "1":
        player = Player()
        player.Namn = getText("Ange namn:", 2,50)
        player.Jersey = getSafeInt("Ange jersey:",1,100)
        player.Team = getText("Ange team:",2,30)
        #player.Age = getSafeInt("Ange age:",0,150)
       
        #listOfPlayers.append(player) - INSERT INTO Players ....
        db.session.add(player)
        db.session.commit()        


    if selection == "4":
        txt = input("Sök efter alla i team:")

        lista = Player.query.filter_by(Team=txt)
        for p in lista:
            print(f"{p.Namn} Nummer: {p.Jersey}  {p.Team}")

    if selection == "5":
        idToEdit = 4
        p = Player.query.filter_by(id=idToEdit).first()
        db.session.delete(p)
        db.session.commit()


    if selection == "3":
        # lista aklla spelare
        # en "väljs"
        idToEdit = 3
        team = "Colorado"
        p = Player.query.filter_by(id=idToEdit).first()
        p.Team = "Colorado"
        p.Namn = "Stefan H"
        db.session.commit()
    if selection == "2":
        for p in Player.query.all():
            print(f"{p.Namn} Nummer: {p.Jersey}  {p.Team}")