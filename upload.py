#!/usr/bin/python3
from client_socket import ClientSocket
import hashlib
import os
import glob
import time

PATH = "/home/pi/Documents/capstone/" #TODO adjust to your project path

eName = PATH+"errorlog.txt" #the errorlog file
try:
    fName = glob.glob(PATH+"*_data.csv")[0]
    print("Got "+fName)#print path to file 
    print(fName[len(PATH):])#print #file name

except IndexError:#no file found
    print("Error")
    with open(eName,'a') as f:
        print("Error no File Found for Upload, Exiting. Time: %i" %time.time(),file=f)
        f.close()
    exit( -1)#error



con = ClientSocket()#start client socket

with open(fName,'r') as f: #open up the file in read mode
        
        data = f.read()
        con.sendName(fName[len(PATH):])#lets the server know which file is to be appended to
        con.send(data)#send the file
        f.close()#close the file

if(con.rec()=='200'):#All clear condition
    print("Data Uploaded and received correctly")
    os.remove(fName)#remove the file from the client
else:
    with open(eName, 'a'):
        print("Error Uploading: Keeping Data. Time: %i"%time.time(),file=f)#Serever did not recive the data, keeping data
        f.close()
con.close()
