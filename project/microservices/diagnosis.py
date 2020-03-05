from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class Diagnosis (db.Model):
    __tablename__ = 'diagnosis'

    QueueID = db.Column(db.String(10), primary_key=True)
    Registration_time = db.Column(db.DateTime, primary_key=True)
    NRIC = db.Column(db.String(10), nullable=False)
    Initial_diagnosis = db.Column(db.String(100))
    Doctor_diagnosis = db.Column(db.String(100))
    Hospital = db.Column(db.String(50), nullable=False)
    Nurse_IC = db.Column(db.String(20), nullable=False)
    Doctor_IC = db.Column(db.String(20), nullable=False)
    Nurse_cleared = db.Column(db.Boolean, nullable=False)
    Severe = db.Column(db.Boolean)
    Complete = db.Column(db.Boolean, nullable=False)

    def __init__(self, QueueID, Registration_time, NRIC, Initial_diagnosis, Doctor_diagnosis, Hospital, Nurse_IC, Doctor_IC, Nurse_cleared, Severe, Complete):
        self.QueueID = QueueID
        self.Registration_time = Registration_time
        self.NRIC = NRIC
        self.Initial_diagnosis = Initial_diagnosis
        self.Doctor_diagnosis = Doctor_diagnosis
        self.Hospital = Hospital
        self.Nurse_IC = Nurse_IC
        self.Doctor_IC = Doctor_IC
        self.Nurse_cleared = Nurse_cleared
        self.Severe = Severe
        self.Complete = Complete

    def json(self):
        return {"QueueID": self.QueueID, 
                "Registration_time": self.Registration_time, 
                "NRIC": self.NRIC, 
                "Initial_diagnosis": self.Initial_diagnosis,
                "Doctor_diagnosis": self.Doctor_diagnosis, 
                "Hospital": self.Hospital, 
                "Nurse_IC": self.Nurse_IC, 
                "Doctor_IC": self.Doctor_IC,
                "Nurse_cleared": self.Nurse_cleared, 
                "Severe": self.Severe, 
                "Complete": self.Complete}


@app.route("/all")
def get_all():
	return jsonify({"cases": [case.json() for case in Diagnosis.query.all()]})



if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5000, debug=True)