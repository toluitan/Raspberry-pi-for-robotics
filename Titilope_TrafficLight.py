import RPi.GPIO as GPIO

import time

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

red = 24

GPIO.setup(red, GPIO.OUT)

green = 18

GPIO.setup(green, GPIO.OUT)

yellow = 23

GPIO.setup(yellow, GPIO.OUT)

while True:

	GPIO.output(red, True)

	time.sleep(0.5)

	GPIO.output(red, False)

	time.sleep(0.5)

	GPIO.output(green, True)

	time.sleep(1)

	GPIO.output(green, False)

	time.sleep(1)

	GPIO.output(yellow, True)

	time.sleep(2)

	GPIO.output(yellow, False)

	time.sleep(2)
