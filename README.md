# Weather Pi
This is the various code for the Weather Pi, a "weather" station Raspberry Pi. The Weather Pi records light, temperature and ambient noise periodically and offloads the data nightly at Midnight UTC to a external server for processing.

This project is for the Colorado School of Mines CSCI 250 Python Based Computing course.

Currently unfinished

# Setup
Download the .py files and the .sh script. Edit the location in the datacapture.py and change the SERVER information in upload.sh 
### Crontab
This project uses crontab to schedule and manage the project.
The pi collects data every 5 minutes and stores it into the _data.csv file, and then uploads the file at Midnight UTC to the external server.

Open cron jobs in edit mode with: 

```
crontab -e
```

Add these lines to cron:
```
*/5 * * * * PATH/LOC_data.csv
* 0 * * * PATH/upload.sh
```
Where PATH is the path to the files and LOC is the location you supplied to the capture script.
These cron jobs run the script every 5 minutes and the upload script at midnight.
# Examples/Output



# Credit
The initial adcUtil script was written by the course instructors, I modified it to be able to use 2 ADC chips on the Raspberry Pi, course web-page available [here](http://cs-courses.mines.edu/csci250/).

Initial script work - [Elijah1111](https://github.com/Elijah1111)
