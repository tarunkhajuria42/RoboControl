import SocketServer
from threading import Thread
import socket
import serial

class service(SocketServer.BaseRequestHandler):
    def handle(self):
        data = 'dummy'
        print "Client connected with ", self.client_address
        ser=serial.Serial(port='COM84', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=1)
        while True:
            data = self.request.recv(1024)
            ser.write(data)
        print "Client exited"
        ser.close()
        self.request.close()

		
class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

t = ThreadedTCPServer((socket.gethostname(),1520), service)
t.serve_forever()