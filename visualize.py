#TODO - 
#figure out epoch utc and first valid time for data

#imports
#color_states funcion based off of "https://medium.com/@erikgreenj/mapping-us-states-with-geopandas-made-simple-d7b6e66fa20d" with edits to change color of state
#for usa shape file see (https://alicia.data.socrata.com/Government/States-21basic/jhnu-yfrj)
import geopandas as gpd
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

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
                time  = np.append(time,tmp[4])
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
                            if (kstep)+val_min-.0001 <= i[j] <= (k+1)step+val_min+.0001: #if value in bin k assign it to color bin k
                                i[j] = blue+(br_step*k)#assign the color
        f.close()#close the data file
    return [all_values,time]
                
                


#color states of interest with the apporpriate color 
def color_states(val_of_int,all_values,index,states = ["CO","NM","MN"]): #all_values as above, value of interest is temp, light, audio, and env, index is the positon in all_values
    if val_of_int == 'temp':#convert val of interest into position in all_values 
        val_of_int == 0
    elif val_of_int == 'light':
        val_of_int == 1
    elif val_of_int == 'audio': 
        val_of_int == 2
    elif val_of_int == 'env':
        val_of_int == 3
        
    #load in shape file and convert to geopandas format
    PATH="/home/elijah/Documents/capstone/"#TODO change path
    usa = gpd.read_file(PATH+"usa_states.shp") # input path of "usa_states.shx"
    
    fig, ax = plt.subplots(figsize=(30,30))

    if 'HI' and 'AK' in states: #exclude hawaii and alaska when possible for clarity
        usa[0,51].plot(ax=ax,alpha=0.3)
    elif 'HI' in states:
        usa[0,50].plot(ax=ax,alpha=0.3)
    elif 'AK' in states:
        usa[1,51].plot(ax=ax,alpha=0.3)
    for n in states: #plot data over selected states with correct color
        if n == 'CO':
            usa[usa.state_abbr == f'{n}'].plot(ax=ax,color = '#' +str(hex(int(co_colors[val_of_int][index])))[2:])
        elif n == 'NM':
            usa[usa.state_abbr == f'{n}'].plot(ax=ax,color = '#' +str(hex(int(nm_colors[val_of_int][index])))[2:])
        elif n == 'MN':
            usa[usa.state_abbr == f'{n}'].plot(ax=ax,color ='#' + str(hex(int(mn_colors[val_of_int][index])))[2:])
    
#animates plot
#def animate_data(start,end,data_file_name, states = ["CO","NM","MN"]):  

temp = np.empty(0)
light = np.empty(0)
audio = np.empty(0)
env = np.empty(0)

start = 1587585602#TODO
end = 1587841802 #last time where data was clean
data_file_name = "GOLDEN_data.csv"


tmp = get_color_data(start, end, data_file_name) #get time values

time_ = tmp[1]

co_colors = tmp[0]#get values for all the states 
nm_colors = tmp[0]
mn_colors = tmp[0]

print(co_colors[0])
#color_states(1,co_colors[0],1)  

#plt.show()
