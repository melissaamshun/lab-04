import paho.mqtt.client as mqtt
import time
from datetime import datetime
import socket

num = 0

def on_connect(client, userdata, flags, rc):
	print("Connected to server with result code "+str(rc))
	client.subscribe("mshun/ping")
	client.message_callback_add("mshun/ping", on_message_from_ping)
    
def on_message(client, userdata, msg):
    	print("Default callback - topic: " + msg.topic + "   msg: " + str(msg.payload, "utf-8"))

#Custom message callback.
def on_message_from_ping(client, userdata, message):
   	print("Receive ping " + message.payload.decode())
   	num = int(message.payload.decode()) + 1    
   	client.publish("mshun/pong", f"{num}")
   	print("Send pong " + f"{num}")
   	time.sleep(2)
        
if __name__ == '__main__':

	#create a client object
	client = mqtt.Client()
	#attach a default callback which we defined above for incoming mqtt messages
	client.on_message = on_message
	#attach the on_connect() callback function defined above to the mqtt client
	client.on_connect = on_connect
	client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
	client.loop_start()
	time.sleep(1)
	
        

