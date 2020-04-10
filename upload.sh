#Uploads the data file
FILE = "*_data.csv"
SERVER = "USER@SERVER"
cat $FILE > tmpD #Backup the data in case the transfer fails
tail -n +2 $FILE > $FILE #Take out the first line of the file
if [scp ./$FILE $SERVER] then
	
	if [ssh $SERVER "cat $FILE >> MASTER$FILE; rm $FILE"]then #append the file to the master list
		echo "Appending Complete"; rm $FILE #remove the file
	else
		echo "$? Error printing Data" >> error.log #hopefully this does not happen but generates a very basic error log
		cat tmpD > $FILE #put the data back into the file 
	fi	
else
	echo "Error in transporting file"
	cat tmpD > $FILE #put the data back into the file 
fi
rm tmpD #remove the backup
