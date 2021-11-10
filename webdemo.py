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



db.create_all()

@app.route("/")
def hello_world():
    txt = "<table>"
    for p in Player.query.all():
        txt += f"<tr><td>{p.Namn}</td><td>Nummer: {p.Jersey}</td><td>{p.Team}</td></tr>"
    txt += "</table>"
    s = f"<html><head></head><body>{txt}</body></html>"
    return s


app.run()    