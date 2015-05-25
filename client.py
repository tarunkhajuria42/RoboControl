# Python Client Script
import socket               # Import socket module
from pygame.joystick import *
import pygame
import math
import time
# Initializing joystick systems
ip=input('Connect the controllers and enter the ip address of the Server')
init()
joystick=[]
for no in range(0,get_count()):		
	joystick.append(Joystick(no)) # Find all Joysticks and initialize them
	joystick[no].init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption('Hello World')
s = socket.socket()         # Create a socket object
port = 1520                # Port for Connection
s.connect((ip, port))
prev=""
fir=True;
# Send to server
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
		sig=raw*-48.99;
		sig=math.floor(sig)+58;
		a.append(chr(int(sig)))
	else:
		sig=raw*49;
		sig=math.floor(sig)+107;
		a.append(chr(int(sig)))
	# Axis Output for Left axis Up/Down
	#Change to pwm 
	raw=joystick[0].get_axis(3)
	if(raw<0):
		sig=raw*-48.99;
		sig=math.floor(sig)+157;
		a.append(chr(int(sig)))
	else:
		sig=raw*49;
		sig=math.floor(sig)+206;
		a.append(chr(int(sig)))
	# Axis Output for Left trigger and right trigger
	if(joystick[0].get_axis(2)>0.4): 
		a.append(chr(5))
	elif(joystick[0].get_axis(2)<-0.4):
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
# Starting for Controller Second
	#Hat Left/Right
	if(joystick[1].get_hat(0)[0]==0):
		a.append(chr(156))
	elif(joystick[1].get_hat(0)[0]==-1):
		a.append(chr(29))
	else:
		a.append(chr(30))
	#Hat Up/Down
	if(joystick[1].get_hat(0)[1]==0):
		a.append(chr(26))
	elif(joystick[1].get_hat(0)[1]==-1):
		a.append(chr(27))
	else:
		a.append(chr(28))
	# Axis Output for Left axis Left Right
	if(joystick[1].get_axis(0)<0.4): 
		a.append(chr(31))
	elif(joystick[1].get_axis(0)>0.4):
		a.append(chr(32))
	else:
		a.append(chr(33))
	# Axis Output for Left axis Up/Down
	if(joystick[1].get_axis(1)<-0.4): 
		a.append(chr(34))
	elif(joystick[1].get_axis(1)>0.4):
		a.append(chr(35))
	else:
		a.append(chr(36))
	# Axis Output for Right axis Up/Dowm
	if(joystick[1].get_axis(3)<-0.4): 
		a.append(chr(43))
	elif(joystick[1].get_axis(3)>0.4):
		a.append(chr(44))
	else:
		a.append(chr(45))
	# Axis Output for Right axis Left/Right
	if(joystick[1].get_axis(4)<-0.4): 
		a.append(chr(40))
	elif(joystick[1].get_axis(4)>0.4):
		a.append(chr(41))
	else:
		a.append(chr(42))
	# Axis Output for Left trigger and right trigger
	if(joystick[1].get_axis(2)>0.4): 
		a.append(chr(37))
	elif(joystick[1].get_axis(2)<-0.4):
		a.append(chr(38))
	else:
		a.append(chr(39))
	# Starting for the buttons
	#A
	if(joystick[1].get_button(0)==1):
		a.append(chr(48))
	else:
		a.append(chr(54))
	#B
	if(joystick[1].get_button(1)==1):
		a.append(chr(49))
	else:
		a.append(chr(55))
	#X
	if(joystick[1].get_button(2)==1):
		a.append(chr(46))
	else:
		a.append(chr(52))
	#Y
	if(joystick[1].get_button(3)==1):
		a.append(chr(47))
	else:
		a.append(chr(53))
	#Left Bumper
	if(joystick[1].get_button(4)==1):
		a.append(chr(50))
	else:
		a.append(chr(56))
	#Right Bumper
	if(joystick[1].get_button(5)==1):
		a.append(chr(51))
	else:
		a.append(chr(57))
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
		s.send(tosend)
	time.sleep(0.1)
s.close()  