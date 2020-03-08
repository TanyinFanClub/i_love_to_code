from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class Ward (db.Model):
    __tablename__ = 'ward'

    NRIC = db.Column(db.String(9), primary_key=True)
    Name = db.Column(db.String(50), nullable=True)
    Diagnosis = db.Column(db.String(100), nullable=False)
    Risks = db.Column(db.String(100), nullable=False)
    Dietary_Requirements = db.Column(db.String(100), nullable=False)
    Timestamp = db.Column(db.DateTime, nullable=False)
    

    def __init__(self, NRIC, Name, NRIC, Diagnosis, Risks, Dietary_Requirements, Timestamp):
        self.NRIC = NRIC
        self.Name = Name
        self.Diagnosis = Diagnosis
        self.Risks = Risks
        self.Dietary_Requirements = Dietary_Requirements
        self.Timestamp = Timestamp


    def json(self):
        return {"NRIC": self.NRIC, 
                "Name": self.Name, 
                "Diagnosis": self.Diagnosis, 
                "Risks": self.Risks,
                "Dietary_Requirements": self.Dietary_Requirements, 
                "Timestamp": self.Timestamp}
            

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5000, debug=True)
