#!/bin/bash

echo "this is a program to manage the fan"
echo 'you can turn on off the fan using "off" or "on"'
echo 'to quit this program use "^C"'

while true; do
	read -p 'Fan option: ' opt
	if [ $opt == "on" ]
	then
		python /home/pi/fan_test_no_interupts.py
		echo "Done"
	else
		if [ $opt == "off" ]
		then
			echo "Turning fan off..."
			python /home/pi/fan_test_fixer.py
			echo "Done"
		else
			echo "Please chose a valid option"
		fi
	fi
done
