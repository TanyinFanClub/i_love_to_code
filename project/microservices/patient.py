from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root@localhost:3306/patient"
## run this code in command line:
## set dbURL=mysql+mysqlconnector://root@localhost:3306/patient 
## python patient.py
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODOFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class Patient(db.Model):
    __tablename__ = 'patient'
    
    nric = db.Column(db.String(9), primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    dob = db.Column(db.Date)
    gender = db.Column(db.String(10))
    race = db.Column(db.String(20))
    nationality = db.Column(db.String(30))
    address = db.Column(db.String(100))
    mobile_number = db.Column(db.String(20))
    home_number = db.Column(db.String(20))
    email = db.Column(db.String(50))
    next_of_kin = db.Column(db.String(50))
    next_of_kin_contact = db.Column(db.String(20))

    def __init__(self, nric, name, dob, gender, race, nationality, address, mobile_number, home_number, email, next_of_kin, next_of_kin_contact):
        self.nric = nric
        self.name = name
        self.dob = dob
        self.gender = gender
        self.race = race
        self.nationality = nationality
        self.address = address
        self.mobile_number = mobile_number
        self.home_number = home_number
        self.email = email
        self.next_of_kin = next_of_kin
        self.next_of_kin_contact = next_of_kin_contact

    def json(self):
        return {"nric": self.nric,
                "name": self.name,
                "dob": self.dob,
                "gender": self.gender,
                "race": self.race,
                "nationality": self.nationality,
                "address": self.address,
                "mobile_number": self.mobile_number,
                "home_number": self.home_number,
                "email": self.email,
                "next_of_kin": self.next_of_kin,
                "next_of_kin_contact": self.next_of_kin_contact}


@app.route("/patient/<string:nric>")
def find_by_nric(nric):
    patient = Patient.query.filter_by(nric=nric).first()
    if patient:
        return jsonify(patient.json())
    return jsonify({"message": "NRIC not found."}), 404


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=6001, debug = True)

