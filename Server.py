import SocketServer
from threading import Thread
import socket

class service(SocketServer.BaseRequestHandler):
    def handle(self):
        data = 'dummy'
        print "Client connected with ", self.client_address
        while True:
            data = self.request.recv(1024)
            for ch in data:
                print(ch+"\n")
        print "Client exited"
        self.request.close()
		
class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

t = ThreadedTCPServer((socket.gethostname(),1520), service)
t.serve_forever()