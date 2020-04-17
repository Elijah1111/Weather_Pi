import socket

#really simple socket client 
class ClientSocket:
    def __init__(self):
        self.conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.conn.connect(("pi.morrissey.dev",25500))
    def send(self, msg):    #sends encoded msg
        self.conn.sendall(msg.encode())
    def rec(self):
        ver = self.conn.recv(1024)  #checks to see if encoded message was received
        if not ver:
            print("bad connection try again")
        else:
            return ver.decode()
    def close(self):
        self.conn.close()   #closes the socket
        
