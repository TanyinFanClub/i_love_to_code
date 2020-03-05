import json
import sys
import os
import pika
import requests

# set host name and port
hostname = 'localhost'
port = 5672

# connect to broker and set up a communication channel
connection = pika.BlockingConnection(pika.ConnectionParameters(host = hostname, port = port))
channel = connection.channel()

# set up exchange name & setting up of exchange if it does not exist
exchangename = 'patient_direct'
channel.exchange_declare(exchange = exchangename, exchange_type='direct')

def receiveID():
    # prepare queue for receiving messages
    channelqueue = channel.queue_declare(queue = 'patient', durable = True)
    queue_name = channelqueue.method.queue
    channel.queue_bind(exchange = exchangename, queue = queue_name, routing_key = 'patient.notification')

    # set up consumer and start to wait for coming messages
    channel.basic_qos(prefetch_count = 1)
    channel.basic_consume(queue = queue_name, on_message_callback = callback, auto_ack = True)
    channel.start_consuming()

def callback(channel, method, properties, body):
    print("Received an order by " + __file__)
    result = processRequest(json.loads(body))
    json.dump(result, sys.stdout, default=str)
    print()
    print()

def processRequest(request):
    print("Processing a request:")
    ### Note! before you send your request to the REST application, make sure you run the patient flask app###

    ## Place request URL to send to patient Flask app
    url = "http://127.0.0.1:6001/patient/" + request

    ## Returns the status code (e.g. <Response[200]>)
    response = requests.get(url)

    ## extract the json data reply using "response.text"
    ## place it in json.loads to keep the json format
    result = json.loads(response.text)
    
    ## invoke replyRequest to send back the reply
    replyRequest(result)
    print(result)

def replyRequest(result):
    hostname = "localhost"
    port = 5672

    connection = pika.BlockingConnection(pika.ConnectionParameters(host = hostname, port = port))
    channel = connection.channel()

    exchangename = "patient_direct"
    channel.exchange_declare(exchange = exchangename, exchange_type = 'direct')
    
    message = json.dumps(result, default = str)

    channel.queue_declare(queue = 'patient_reply', durable = True)
    channel.queue_bind(exchange = exchangename, queue = 'patient_reply', routing_key = "patient.reply")
    channel.basic_publish(exchange = exchangename, routing_key = 'patient.reply', body = message, properties = pika.BasicProperties(delivery_mode = 2))

    print ("Details sent back to notification")
    # print(message)
    
if __name__ == "__main__":
    print("This is " + os.path.basename(__file__) + ": waiting for a request")
    receiveID()
