from client_socket import ClientSocket
import hashlib
import os
import glob

print("Uploading Data")
fName = glob.glob("*.csv")[0]
print("Got "+fName)

con = ClientSocket()#start client socket
with open(fName,'r') as f: #open up the file in read mode
        data = f.read()
        con.sendName(fName)#lets the server know which file is to be appended to
        con.send(data)#send the file
        f.close()#close the file
if(con.rec()=='200'):#All clear condition
    print("Data Uploaded and received correctly")
    os.remove(fName)#remove the file its on the server
else:
    print("Error Uploading: Keeping Data")#Serever did not recive the data keeping data
con.close()
