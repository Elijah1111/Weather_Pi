# Weather Pi
This is the various code for the Weather Pi, a "weather" station Raspberry Pi. The Weather Pi records light, temperature and ambient noise periodically and offloads the data nightly at Midnight to an external server for processing.

This project is for the Colorado School of Mines CSCI 250 Python Based Computing course.

# Setup
Download the .py files.Make sure the python packages listed below are installed.

Edit LOC in the dataCapture.py and PATH in both upload.py and dataCapture.py, They are marked with a TODO.

Make upload.py and dataCapture.py executable with chmod.
```
chmod +x upload.py dataCapture.py
```
Then setup the cron jobs.

### Crontab
This project uses crontab to schedule and manage the project.
The pi collects data every 5 minutes and stores it into the _data.csv file, and then uploads the file at Midnight to the external server.

Open cron jobs in edit mode with: 

```
crontab -e
```

Add these lines to cron:
```
*/5 * * * * PATH/dataCapture.py
0 0 * * * PATH/upload.py
```
Where PATH is the path to the project.
For example:
```
*/5 * * * * /home/pi/Documents/capstone/dataCapture.py
```
These cron jobs run the script every 5 minutes and the upload script at midnight.

# Examples/Output
Here is an example of the output csv file.

Temp,Light,Audio,AudioEnv,Time
```
16.774,1.068,0.008,0.042,1587152617
16.774,1.068,0.005,0.039,1587152618
16.452,1.068,0.015,0.045,1587152619
16.774,1.068,0.002,0.042,1587152619
```
Once the data is collected the visualization script can be used to generate plots of the data. These plots can be used to show trends in the sensors of the pi.

# Python Packages
### For Visualization 
[GeoPandas](https://geopandas.org/)

[Pandas](https://pandas.pydata.org/pandas-docs/stable/)

[MatPlotLib](https://matplotlib.org/3.2.1/contents.html)
### For Proccessing
[Numpy](https://numpy.org/doc/)
# Credit
The initial adcUtil script was written by the course instructors, I modified it to be able to use 2 ADC chips on the Raspberry Pi, course web-page available [here](http://cs-courses.mines.edu/csci250/).

Initial script work - [Elijah1111](https://github.com/Elijah1111)

Socket server work - [Liam Morrissey](https://github.com/liam-morrissey)

Initial visual script work - Alexander Wilson
