#!/bin/bash

echo "this is a program to manage the fan"
echo 'you can turn on off the fan using "off" or "on"'
echo 'to quit this program use "^C"'

while true; do
	read -p 'Fan option: ' opt #reads the option the user wants
	if [ $opt == "on" ] #if the option the user wants is on
	then
		echo "Turning fan on..."
		python ./fan_on.py #run the python program
		echo "Done"
	else
		if [ $opt == "off" ] #if the option the user wants is off
		then
			echo "Turning fan off..."
			python ./fan_off.py #run the python program
			echo "Done"
		else #if what is entered is anything other than on or off
			echo "Please chose a valid option" #complain to the user
		fi
	fi
done
