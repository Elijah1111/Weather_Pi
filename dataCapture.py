import time
import adcUtil as adc
from os import path
#TODO edit anything with a TODO
#~~~~~~~~~~~~~~~~~~~~Assignment~~~~~~~~~~~~~~~~~~~~~~~~~~~~
location = "GOLDEN" #TODO Change me based on location
fName = "data_"+location+".csv" #set up the file name 

tChan = (0,0)#Channel 0, chip 0
iChan = (1,0)
lChan = (0,1)#Channel 0,  chip 1
#~~~~~~~~~~~~~~~~~~~~Functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def readTemp():#TODO
    tmp = adc.readADC(tChan[0],tChan[1])
    return (100*tmp -50)#equation for tempature

def readInfer():#TODO 
    return adc.readADC(iChan[0],iChan[1])

def readLight():#TODO
    return adc.readADC(lChan[0],lChan[1])
#~~~~~~~~~~~~~~~~~~~~Main~~~~~~~~~~~~~~~~~~~~~~~~~~~~

tmp = ("{:.3f},".format(readTemp())+#Record Temperature
        "{:.3f},".format(readInfer())+#Record Infer-red
        "{:.3f},".format(readLight())+#Record Light
       "{:.0f}".format(time.time()))#Record time in epoch UTC
flag=False
if(not path.exists(fName)):#prints the header if the file does not exist
    flag=True

with open(fName,'a') as f: #open up the file in append mode
    if(flag):print("Temp,IR,Light,Time",file=f)#print header

    print(tmp, file=f)#print this in the file
    f.close()
