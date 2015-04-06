# Script for testing the xbox 360 joystick
from pygame.joystick import *
import pygame
import time
init()
joystick=Joystick(0)
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption('Hello World')
joystick.init()
while True:
	for event in pygame.event.get():
		nothing=0
	for i in range(0,1):
		print joystick.get_axis(i)
		a=''
		a.'
	time.sleep(0.01)