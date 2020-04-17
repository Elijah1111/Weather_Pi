from client_socket import ClientSocket
import hashlib
import os
import glob

print("Uploading Data")
fName = glob.glob("*.csv")[0]
print("Got "+fName)

con = ClientSocket()
hString="0"
result = hashlib.md5(hString.encode())
checksum = result.digest()

with open(fName,'r') as f: #open up the file in read mode
        con.send(checksum)
        con.send(f.read())
        f.close()

if(con.rec()==200):
    print("Data Uploaded and received correctly")
    os.remove(fName)
else:
    print("Error Uploading: Keeping Data")

con.close()
