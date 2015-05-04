import SocketServer
from threading import Thread
import socket
import serial
import time

class service(SocketServer.BaseRequestHandler):
	def handle(self):
		data = 'dummy'
		while True:
			data = self.request.recv(1024)
			print(data)
		print "Client exited"
		self.request.close()

		
class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
	pass
print "Started"
t = ThreadedTCPServer((socket.gethostname(),1520), service)
t.serve_forever()