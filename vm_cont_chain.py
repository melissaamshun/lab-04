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
   	time.sleep(1)    
   	client.publish("mshun/pong", f"{num}")
   	print("Send pong " + f"{num}")
   	
        
if __name__ == '__main__':

	hostname = socket.gethostname()
	ip_address = socket.gethostbyname(hostname)
	
	client = mqtt.Client()
	

	#create a client object
	
	#attach a default callback which we defined above for incoming mqtt messages
	client.on_message = on_message
	#attach the on_connect() callback function defined above to the mqtt client
	client.on_connect = on_connect
	client.connect(host="6172.20.10.8", port=1883, keepalive=60)
	client.loop_forever()
        

