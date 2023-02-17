import paho.mqtt.client as mqtt
import time
from datetime import datetime
import socket

num = 0

def on_connect(client, userdata, flags, rc):
	print("Connected to server with result code "+str(rc))
	client.subscribe("mshun/pong")
	client.message_callback_add("mshun/pong", on_message_from_pong)
	client.publish("mshun/ping", f"{num}")
	print("Send ping " + f"{num}")
	time.sleep(1)
	
    
def on_message(client, userdata, msg):
    	print("Default callback - topic: " + msg.topic + "   msg: " + str(msg.payload, "utf-8"))

#Custom message callback.
def on_message_from_pong(client, userdata, message):
   	print("Receive pong " + message.payload.decode())
   	num = int(message.payload.decode()) + 1    
   	time.sleep(1)
   	client.publish("mshun/ping", f"{num}")
   	print("Send ping " + f"{num}")
   	
    
if __name__ == '__main__':

	num = 0
	
	client = mqtt.Client()
	
	
	#attach a default callback which we defined above for incoming mqtt messages
	client.on_message = on_message
	#attach the on_connect() callback function defined above to the mqtt client
	client.on_connect = on_connect
							
	client.connect(host="172.20.10.8", port=1883, keepalive=60)
	client.loop_start()
	
	
	while True:
		pass
	
	
		
		
		
		
        
