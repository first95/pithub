#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode(GPIO.BCM)

SWITCH_PIN = 15
LED_PIN = 4

GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, 1)
#GPIO.cleanup()

