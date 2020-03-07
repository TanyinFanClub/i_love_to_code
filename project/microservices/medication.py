from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
import pika
import requests
import json
import sys

app = Flask(__name__)
#TESTING
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/esd_project' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Actual
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
# app.config['SQLALCHEMY_TRACK_MODOFICATIONS'] = False

#Set up for AMPQ
# set host name and port
hostname = 'localhost'
port = 5672

# connect to broker and set up a communication channel
connection = pika.BlockingConnection(pika.ConnectionParameters(host = hostname, port = port))
channel = connection.channel()

# set up exchange name & setting up of exchange if it does not exist
exchangename = 'patient_direct'
channel.exchange_declare(exchange = exchangename, exchange_type='direct')

db = SQLAlchemy(app)
CORS(app)

class Prescription(db.Model):
    __tablename__ = 'Prescription'
    
    QueueID = db.Column(db.String(10), primary_key = True)
    Registration_timestamp = db.Column(db.Date, primary_key=True)
    NRIC = db.Column(db.String(9),nullable=False)
    Medication_ID = db.Column(db.String(10))

    def __init__(self, QueueID, Registration_timestamp, NRIC, Medication_ID):
        self.QueueID = QueueID
        self.Registration_timestamp = Registration_timestamp
        self.NRIC = NRIC
        self.Medication_ID = Medication_ID

    def json(self):
        return {"QueueID": self.QueueID,
                "Registration_timestamp": self.Registration_timestamp,
                "NRIC": self.NRIC,
                "Medication_ID": self.Medication_ID
                }
class Medication(db.Model):
    __tablename__ = 'Medication'
    
    Medication_ID  = db.Column(db.String(10), primary_key = True)
    Medicine_name  = db.Column(db.String(100), nullable=False)
    Quantity = db.Column(db.INT,nullable=False)
    Description = db.Column(db.String(100),nullable=False)

    def __init__(self, Medication_ID, Medicine_name, Quantity, Description):
        self.Medication_ID = Medication_ID
        self.Medicine_name = Medicine_name
        self.Quantity = Quantity
        self.Description = Description

    def json(self):
        return {"Medication ID": self.Medication_ID,
                "Medicine Name": self.Medicine_name,
                "Quantity": self.Quantity,
                "Description": self.Description
                }
#Return the list of medicine                  
@app.route("/medicine")
def receive_medication_list():
    return jsonify({"Medicine": [medicine.json() for medicine in Medication.query.all()]})


if __name__ =='__main__': #It will run as a flask app if it is being imported.
    app.run(port=6969,debug=True)