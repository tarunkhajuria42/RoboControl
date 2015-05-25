# Script for testing the xbox 360 joystick
from pygame.joystick import *
import pygame
import time
import math

init()
joystick=Joystick(0)
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption('Hello World')
joystick.init()
while True:
	for event in pygame.event.get():
		nothing=0
	raw=joystick.get_axis(3)
	if(raw<0):
		sig=raw*-48.99;
		print(math.floor(sig))
		sig=math.floor(sig)+157;
		print(int(sig))
	else:
		sig=raw*49;
		print(math.floor(sig))
		sig=math.floor(sig)+206;
		print(int(sig))
	time.sleep(0.01)