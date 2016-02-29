#!/bin/bash

while [ 1 ]; do
	ps aux | grep udhcpd | grep -v grep > /dev/null # returns 1 if not found

	if [ $? == 1 ]; then
		/home/pi/switch_handler/led_off.py 2> /dev/null
	else
		/home/pi/switch_handler/led_on.py 2> /dev/null
	fi
	sleep 0.5
done
