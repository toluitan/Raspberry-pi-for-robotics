
import RPi.GPIO as GPIO
import time

motor_a = 17
motor_b = 18
motor_c = 4
motor_d = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor_a, GPIO.OUT)
GPIO.setup(motor_b, GPIO.OUT)
GPIO.setup(motor_c, GPIO.OUT)
GPIO.setup(motor_d, GPIO.OUT)

while True:

	GPIO.output(motor_a, True)
	GPIO.output(motor_b, False)
	GPIO.output(motor_c, False)
	GPIO.output(motor_d, True)
	time.sleep(5)

	GPIO.output(motor_a, True)
        GPIO.output(motor_b, True)
	GPIO.output(motor_c, True)
	GPIO.output(motor_d, True)
        time.sleep(3)

	# turning the motor in reverse
	GPIO.output(motor_a, False)
        GPIO.output(motor_b, True)
	GPIO.output(motor_c, True)
	GPIO.output(motor_d, False)
        time.sleep(5)

	GPIO.output(motor_a, True)
        GPIO.output(motor_b, True)
	GPIO.output(motor_c, True)
	GPIO.output(motor_c, True)
        time.sleep(3)
