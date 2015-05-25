# Python Client Script
import socket               # Import socket module
import math
import time
s = socket.socket()         # Create a socket object
port = 1520            # Reserve a port for your service.
s.connect(("127.0.0.1", port))
print "connected"
prev=time.time()
a="1"
while True:
        print "receiving\n"
        print s.recv(1024)
s.close()  
