# Weather Pi
This is the various code for the Weather Pi, a "weather" station Raspberry Pi. The Weather Pi records light, tempature and ambient noise every periods and offloads the data nightly at Midnight UTC to a external server for proccessing.

This project is for the Colorado School of Mines CSCI 250 Python Based Computing course.



# Setup
Download the .py files and the .sh script.
## Crontab
Ths project uses crontab to schedual and manage the project.
The pi collects data every 5 minutes and stores it into the _data.csv file, and then uploads the file at Midnight UTC to the external server.


NOT FINISHED

# Examples



# Credit
The intial adcUtil script was written by the course instructors, I modified it to be able to use 2 ADC chips on the Raspberry Pi.

Initial script work - [Elijah1111](https://github.com/Elijah1111)
