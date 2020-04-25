#!/usr/bin/python3
import time
import modADC as adc #import the modified adc code 
from os import path

#TODO edit anything with a TODO
#~~~~~~~~~~~~~~~~~~~~Assignment~~~~~~~~~~~~~~~~~~~~~~~~~~~~

LOC = "GOLDEN" #TODO Change me based on location
PATH = "/home/pi/Documents/capstone/"#TODO adjust to the path of your project
fName = PATH+LOC+"_data.csv" #set up the file name 


tChan = (0,0)#Channel 0, chip 0 Temperature
lChan = (1,0)#Channel 1, chip 0 Light
aChan = (0,1)#Channel 0,  chip 1 Audio
eChan = (1,1)#Channel 1,  chip 1 Envelope

#~~~~~~~~~~~~~~~~~~~~Functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def readTemp():#Read thermometer
    tmp = adc.readADC(tChan[0],tChan[1])
    return (100*tmp -50) #Change Volts to deg. C

def readAud():#Read Audio
    return (adc.readADC(aChan[0],aChan[1])-1.65) #-1.65 to adjust audio voltage to 0

def readEnv():#Read Audio Envelope
    return adc.readADC(eChan[0],eChan[1])

def readLight():#Read Photoresistor
    return adc.readADC(lChan[0],lChan[1])

#~~~~~~~~~~~~~~~~~~~~Main~~~~~~~~~~~~~~~~~~~~~~~~~~~~

tmp = ("{:.3f},".format(readTemp())+#Record Temperature
        "{:.3f},".format(readLight())+#Record Light
        "{:.3f},".format(readAud())+#Record Audio
        "{:.3f},".format(readEnv())+#Record Audio Envelope
       "{:.0f}".format(time.time()))#Record time in epoch UTC

with open(fName,'a') as f: #open up the file in append mode
    print(tmp, file=f)#print this in the file
    f.close()

print("Data Collected")
