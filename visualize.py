#TODO - 
#figure out epoch utc and first valid time for data

#imports
#color_states funcion based off of "https://medium.com/@erikgreenj/mapping-us-states-with-geopandas-made-simple-d7b6e66fa20d" with edits to change color of state
#for usa shape file see (https://alicia.data.socrata.com/Government/States-21basic/jhnu-yfrj)
import geopandas as gpd
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt
import matplotlib.colors as mcol
import matplotlib.cm as cm
import pandas as pd
import numpy as np
import glob
from datetime import datetime
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!! edit to include location dependency!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def get_color_data(start, end, data_file_name): #takes in data from file and maps colors on red-blue scale for coloring in future sections, only for one location  
    with open(data_file_name) as f:
        lines = f.readlines() #get data from file
        temp = np.empty(0)
        light = np.empty(0)
        audio = np.empty(0)
        env = np.empty(0)
        time = np.empty(0)
        for i in range(len(lines)):
            tmpy = lines[i].split(',')
            tmp = (float(tmpy[0]),float(tmpy[1]),float(tmpy[2]),float(tmpy[3]),int(tmpy[4].rstrip()))
            if start <= tmp[4] <= end: #if data in time range as well as time values
                
                temp  = np.append(temp,tmp[0])
                light = np.append(light,tmp[1])
                audio = np.append(audio,tmp[2])
                env   = np.append(env,tmp[3])
                time   = np.append(time,tmp[4])
                
        all_values = [temp,light,audio,env]
        blue = int(0x0000FF)#create 9 color bins of colors varing between red and blue
        red = int(0xFF0000)
        br_step = int((red-blue)/1000)
        for i in all_values:
                val_max = max(i) #find the max of the current array 
                val_min = min(i) #find the min of the current array
                val_range = val_max-val_min #create mapping between min and max values and create a corrisponding color array
                step = val_range/1000#create 9 value bins
                for j in range(len(i)):
                    for k in range(1000):
                        if (((k*step)+val_min-.0001) <= i[j] and i[j] <= ((k+1)*step+val_min+.0001)): #if value in bin k assign it to color bin k
                            i[j] = blue+(br_step*k)#assign the color
        f.close()#close the data file
    return [all_values,time]
                
                


#color states of interest with the apporpriate color 
def color_states(val_of_int,all_values,index,t,states = ["CO","NM","MN"]): #all_values as above, value of interest is temp, light, audio, and env, index is the positon in all_values
    #load in shape file and convert to geopandas format
    PATH="/home/elijah/Documents/capstone/"#TODO change path
    usa = gpd.read_file(PATH+"usa_states.shp") # input path of "usa_states.shx"
    
    fig, ax = plt.subplots(figsize=(5,5),dpi=150)
    s=""#empty string
    if val_of_int == 0:
        s = "Temprature" 
    if val_of_int == 1:
        s = "Light"
    if val_of_int == 2:
        s = "Audio"
    if val_of_int == 3:
        s = "Audio Envelope"
    plt.title(s + ' ' + str(datetime.fromtimestamp(t)))
    for n in states: #plot data over selected states with correct color
        if n == 'CO':
            val = str(hex(int(all_values[0][val_of_int][index])))[2:].zfill(6)
            print(n + " VAL: " + val)
            usa[usa.state_abbr == f'{n}'].plot(ax=ax,color = '#' + val)
        elif n == 'NM':
            val = str(hex(int(all_values[1][val_of_int][index])))[2:].zfill(6)
            print(n + " VAL: " + val)
            usa[usa.state_abbr == f'{n}'].plot(ax=ax,color = '#' + val)
        elif n == 'MN':
            val = str(hex(int(all_values[2][val_of_int][index])))[2:].zfill(6)
            print(n + " VAL: " + val)
            usa[usa.state_abbr == f'{n}'].plot(ax=ax,color ='#' + val)
    plt.colorbar(fig) 
    fig.savefig(PATH+"image/"+str(val_of_int)+'_'+str(index)+".png")#save figure
    print("Image saved")
    plt.close(fig)



start = 1587585602#TODO
end = 1587844502#last time where data was clean

tmp=glob.glob("*.csv")
print(tmp)

mn_colors = get_color_data(start, end, tmp[0])[0] # get the data for mn

val = get_color_data(start, end, tmp[1]) # get the data for nm

nm_colors = val[0]

co_colors = get_color_data(start, end, tmp[2])[0] # get the data for co
del tmp # remove tmp free up space 
vals= [co_colors, mn_colors, nm_colors]

del mn_colors
del co_colors

for i in range(len(nm_colors)):
    for j in range(0,nm_colors[i].size,19):
        color_states(i,vals,j,val[1][j])

print("Finished saving files")
