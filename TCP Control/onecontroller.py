# Python Client Script
import socket               # Import socket module
from pygame.joystick import *
import pygame
import math
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
port = 1520                # Reserve a port for your service.
s.connect(("10.0.1.70", port))
# Send to server
debug=open("debog.txt",'w')
prev=""
fir=True;
while True:
	tosend=""
	for event in pygame.event.get():
		nothing=0
	a=[]
	# Joystick 1 Control
	#Hat Left/Right
	if(joystick[0].get_hat(0)[0]==0):
		a.append(chr(255))
	elif(joystick[0].get_hat(0)[0]==-1):
		a.append(chr(3))
	else:
		a.append(chr(4))
	#Hat Up/Down
	if(joystick[0].get_hat(0)[1]==0):
		a.append(chr(0))
	elif(joystick[0].get_hat(0)[1]==-1):
		a.append(chr(1))
	else:
		a.append(chr(2))
	# PWM Output for Axis
	raw=joystick[0].get_axis(1)
	if(raw<0):
		sig=raw*-98;
		sig=math.floor(sig)+58;
		a.append(chr(int(sig)))
	else:
		sig=raw*98;
		sig=math.floor(sig)+157;
		a.append(chr(int(sig)))
	# Axis Output for Left axis Up/Down
	if(joystick[0].get_axis(3)<0.4): 
		a.append(chr(11))
	elif(joystick[0].get_axis(3)>0.4):
		a.append(chr(12))
	else:
		a.append(chr(13))
	# Axis Output for Left axis Left/Right
	if(joystick[0].get_axis(4)<0.4): 
		a.append(chr(8))
	elif(joystick[0].get_axis(4)>0.4):
		a.append(chr(9))
	else:
		a.append(chr(10))
	# Axis Output for Left trigger and right trigger
	if(joystick[0].get_axis(2)<0.4): 
		a.append(chr(5))
	elif(joystick[0].get_axis(2)>0.4):
		a.append(chr(6))
	else:
		a.append(chr(7))
	# Starting for the buttons
	#A
	if(joystick[0].get_button(0)==1):
		a.append(chr(16))
	else:
		a.append(chr(22))
	#B
	if(joystick[0].get_button(1)==1):
		a.append(chr(17))
	else:
		a.append(chr(23))
	#X
	if(joystick[0].get_button(2)==1):
		a.append(chr(14))
	else:
		a.append(chr(20))
	#Y
	if(joystick[0].get_button(3)==1):
		a.append(chr(15))
	else:
		a.append(chr(21))
	#Left Bumper
	if(joystick[0].get_button(4)==1):
		a.append(chr(18))
	else:
		a.append(chr(24))
	#Right Bumper
	if(joystick[0].get_button(5)==1):
		a.append(chr(19))
	else:
		a.append(chr(25))
	if(fir):
		this="".join(a)
		prev=this
		s.send(this)
		fir=False
	else:
		this="".join(a)
		for cnt in range(0,len(this)):
			if(this[cnt]!=prev[cnt]):
				tosend=tosend+this[cnt]
		prev=this
		print(len(tosend))		
		s.send(tosend)
	debug.write(tosend+"\n")
	time.sleep(0.1)
s.close()  
debug.close()