# Python Client Script
import socket               # Import socket module
from pygame.joystick import *
import pygame
import time
# Initializing joystick systems
init()
joystick=[]
for no in range(0,get_count()):		
	joystick.append(Joystick(no)) # Find all Joysticks and initialize them
	joystick[no].init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption('Hello World')
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 1520                # Reserve a port for your service.
s.connect((host, port))
# Send to server
while True:
	a=[]
	a.append(chr(1))
	a.append(chr(2))
	s.send("".join(a))
s.close  