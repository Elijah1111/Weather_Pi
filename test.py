from client_socket import ClientSocket

cs = ClientSocket()
cs.send("Yo")
cs.send("This is a test")
cs.rec()
cs.close()
