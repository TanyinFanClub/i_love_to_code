# Notification Microservice functionalities:
# 1) Request NOK information (SMS to NOK)
# 2) Request Patient Info (Email)
# 3) Send Email
# 4) Send SMS 

import json
import sys
import os
import random
import datetime
import plivo
# email API
from mailjet_rest import Client
# email API Keys here
mailjet = Client(auth=(api_key, api_secret), version='v3.1')

#SMS API



# URLs
import requests
patientURL = 'http://localhost:6000/patient/'

# email Request-Reply with Patient Microservice
@app.route("/notification/email/<string:nric>", methods=['POST'])

def recieveEmailNotification(nric):
    #concatenate URL to include NRIC
    patientURL = patientURL + nric
    #send request to Patient Microservice
    r = requests.post(patientURL, json = order)
    print("Request for Patient Details sent")
    #retrieve results from Patient Microservice
    result = json.loads(r.text.lower())
    if result["status"]:
        email_address = result["email"]
        patient_name = result["name"]
        # email API syntax
        data = {
            'Messages': [
                {
                "From": {
                    "Email": "shlai.2018@smu.edu.sg",
                    "Name": "See Hoe"
                },
                "To": [
                    {
                    "Email": email_address,
                    "Name": patient_name
                    }
                ],
                "Subject": "Diagnosis Report",
                "TextPart": "Diagnosis Report",
                "HTMLPart": "<h3>Dear "+ patient_name + ",</h3><br />Attached is your diagnosis report. Thank You.",
                "CustomID": "Test"
                }
            ]
            }
        mail_result = mailjet.send.create(data=data)
        print(mail_result.status_code)
        print(mail_result.json())
    else:
        print("Patient not Found")
    return result


# SMS Request Reply with Patient micro service
@app.route("/notification/sms/<string:nric>", methods=['POST'])
def recieveSMSNotification(nric):
    #concatenate URL to include NRIC
    patientURL = patientURL + nric
    #send request to Patient Microservice
    r = requests.post(patientURL, json = order)
    print("Request for Patient Details sent")
    #retrieve results from Patient Microservice
    result = json.loads(r.text.lower())
    if result["status"]:
        # input SMS API syntax stuff here please
        client = plivo.RestClient("MAMTQ5NTQ4ZWZIZJC4NG", "MTAwYWJmNmM2MTJlM2Y1YmZiY2U4ZjJmNDY3OTdk")
        response = client.messages.create(
            src='', #Sender Phone Number
            dst='', #Receiver Phone Number
            text=MSG_TO_SEND,
            url='http://foo.com/sms_status/',
            )
        print(response)
        # prints only the message_uuid
        print(response.message_uuid)
        pass
    else:
        print("Patient not Found")
    return result


# running it as a script 
if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=6006, debug = True)