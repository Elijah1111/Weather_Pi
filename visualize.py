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

def get_color_data(start, end, data_file_name): #takes in data from file and maps colors on red-blue scale for coloring in future sections, only for one location  
    with open(data_file_name) as f:
        lines = f.readlines() #get data from file
        

        temp = np.empty(0)
        light = np.empty(0)
        audio = np.empty(0)
        env = np.empty(0)
        time = np.empty(0)
        
        for i in range(len(lines)):
            tmpy = lines[i].split(',')#split the csv files
            tmp = (float(tmpy[0]),float(tmpy[1]),float(tmpy[2]),float(tmpy[3]),int(tmpy[4].rstrip()))
            if start <= tmp[4] <= end: #if data in time range save it
                
                temp  = np.append(temp,tmp[0])
                light = np.append(light,tmp[1])
                audio = np.append(audio,tmp[2])
                env   = np.append(env,tmp[3])
                time   = np.append(time,tmp[4])
                
        all_values = [temp,light,audio,env]
        f.close()#close the data file
    return [all_values,time]
                
                


#color states of interest with the apporpriate color 
def color_states(val_of_int,all_values,index,t,states = ["CO","NM","MN"]): #all_values as above, value of interest is temp, light, audio, and env, index is the positon in all_values
    #load in shape file and convert to geopandas format

    PATH="/home/elijah/Documents/capstone/"#TODO change path
    
    usa = gpd.read_file(PATH+"usa_states.shp") # input path of "usa_states.shx"
    
    # Make a user-defined colormap.
    cm1 = mcol.LinearSegmentedColormap.from_list("MyCmapName",["b","r"])
    
    maxVal = all_values[0][val_of_int][0]#set max and min floaters
    minVal = maxVal
    
    for i in all_values:#grab states max and min
        tmp = i[val_of_int].max()
        if(tmp > maxVal):
            maxVal = tmp
        tmp = i[val_of_int].min()
        if(tmp < minVal):
            minVal = tmp

    cnorm = mcol.Normalize(vmin=minVal,vmax=maxVal)#setup color noramalization
    cpick = cm.ScalarMappable(norm=cnorm,cmap=cm1)#setup the scale
    cpick.set_array([])
    
    fig, ax = plt.subplots(figsize=(5,5),dpi=150)#setup figure
    
    s=""#title string
    if val_of_int == 0:
        s = "Temperature" 
    if val_of_int == 1:
        s = "Light"
    if val_of_int == 2:
        s = "Audio"
    if val_of_int == 3:
        s = "Audio Envelope"

    plt.title(s + ' ' + str(datetime.fromtimestamp(t)))#value and date title
    
    for n in states: #plot data over selected states with correct color
        if n == 'CO':
            val = all_values[0][val_of_int][index]
            print(n + " VAL: " + str(val))
            usa[usa.state_abbr == f'{n}'].plot(ax=ax,color = cpick.to_rgba(val))
        elif n == 'NM':
            val = all_values[0][val_of_int][index]
            print(n + " VAL: " + str(val))
            usa[usa.state_abbr == f'{n}'].plot(ax=ax,color = cpick.to_rgba(val))
        elif n == 'MN':
            val = all_values[0][val_of_int][index]
            print(n + " VAL: " + str(val))
            usa[usa.state_abbr == f'{n}'].plot(ax=ax,color = cpick.to_rgba(val))
   
    plt.colorbar(cpick)#make the color bar
    fig.savefig(PATH+"image/"+str(val_of_int)+'_'+str(index)+".png")#save figure
    print("Image saved")
    plt.close(fig)#close the figure save space


#TODO select the time you need
start = 1587585602#Time to start taking data
end = 1587844502#last time where data was clean

tmp=glob.glob("*.csv")#grab csv files
print(tmp)


mn_colors = get_color_data(start, end, tmp[0])[0] # get the data for mn

val = get_color_data(start, end, tmp[1]) # get the data for nm and the time

nm_colors = val[0]

co_colors = get_color_data(start, end, tmp[2])[0] # get the data for co
del tmp # remove tmp free up space 

vals= [co_colors, mn_colors, nm_colors]#put these together

del mn_colors
del co_colors
#saved nm because it was the smallest

for i in range(len(nm_colors)):#make the plots
    for j in range(0,nm_colors[i].size):
        color_states(i,vals,j,val[1][j])

print("Finished saving files")
