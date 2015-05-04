# Python Client Script
import socket               # Import socket module
import math
import time
s = socket.socket()         # Create a socket object
port = 1520                # Reserve a port for your service.
s.connect(("10.0.1.70", port))
prev=time.time()
a="1"
while True:
	if(time.time()-prev>10):
		prev=time.time()
		if(a=="1"):
			a="0"
		else:
			a="1"
	s.send(a)
s.close()  