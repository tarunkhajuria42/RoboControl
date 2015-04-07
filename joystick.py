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
	print joystick.get_axis(1)
	time.sleep(0.01)