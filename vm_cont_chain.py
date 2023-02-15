import paho.mqtt.client as mqtt
import time
from datetime import datetime
import socket

"""This function (or "callback") will be executed when this client receives 
a connection acknowledgement packet response from the server. """
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    
    client.subscribe("mshun/ping")
    
    #Add the custom callbacks by indicating the topic and the name of the callback handle
    client.message_callback_add("mshun/ping", on_message_from_ping)

def on_message(client, userdata, msg):
    print("Default callback - topic: " + msg.topic + "   msg: " + str(msg.payload, "utf-8"))

def on_message_from_ping(client, userdata, message):
   print("Receiving ping: "+message.payload.decode())
   
if __name__ == '__main__':
    
    #get IP address
    """your code here"""
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    
    #create a client object
    client = mqtt.Client()   
    #attach a default callback which we defined above for incoming mqtt messages
    client.on_message = on_message
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect
    
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    
    client.loop_start()
    time.sleep(1)
    
    num = 0
        
    while True:
    
    	client.publish("mshun/pong", f"{num}")
    	print("Sending pong " + str(num))
    	time.sleep(4)
        
        
        
        
        

