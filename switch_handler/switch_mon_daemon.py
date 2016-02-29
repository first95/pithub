#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode(GPIO.BCM)

SWITCH_PIN = 15
LED_PIN = 4

GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)


print GPIO.input(SWITCH_PIN)
GPIO.output(LED_PIN, 1)
time.sleep(1)
GPIO.output(LED_PIN, 0)

#As expected, 0 is LED on, 1 is off.
#For the switch, 0 corresponds to the green position.

DEBOUNCE_TIME_S = 0.01
try:
	prev_on = False;
	while True:
		time.sleep(DEBOUNCE_TIME_S)
		on = (GPIO.input(SWITCH_PIN) == 0)
		if on and not prev_on:
			print "Switching on"
			subprocess.call('/home/pi/switch_handler/turn_on_dhcp_server.sh')
		elif not on and prev_on: 
			print "Switching off."
			subprocess.call('/home/pi/switch_handler/turn_off_dhcp_server.sh')
		prev_on = on
		
except KeyboardInterrupt:
	print "Cleaning up"
GPIO.cleanup()

