import socket
import hashlib
#really simple socket client 
class ClientSocket:
    def __init__(self):
        self.conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.conn.connect(("192.168.0.74",25500))
    def sendName(self, name):
        self.conn.sendall(name.encode())
    def send(self, msg):    #sends encoded msg
        data = msg.encode()
        check = hashlib.md5(data).digest()[0:2]
        self.conn.send(check)
        self.conn.sendall(data)
    def rec(self):
        ver = self.conn.recv(1024)  #checks to see if encoded message was received
        if not ver:
            print("bad connection try again")
        else:
            return ver.decode()
    def close(self):
        self.conn.close()   #closes the socket
        
