#Test script for writing to arduino
import serial
import time
ser=serial.Serial(port='COM74', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=1)
a=chr(1)
while True:
	ser.write(chr(230))
	time.sleep(0.01)
	ser.write(chr(255))
	time.sleep(0.005)
ser.close()

