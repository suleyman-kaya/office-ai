import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)


relay_1 = 17
relay_2 = 27
relay_3 = 22
relay_4 = 26

def role_ac(relay):
	GPIO.output(relay, GPIO.LOW)

def role_kapa(relay):
	GPIO.output(relay, GPIO.HIGH)

"""
while True:
	role_ac(relay_1)
	sleep(1)
	role_ac(relay_2)
	sleep(1)
	role_ac(relay_3)
	sleep(1)
	role_ac(relay_4)
	sleep(1)
	role_kapa(relay_1)
	role_kapa(relay_2)
	role_kapa(relay_3)
	role_kapa(relay_4)
	sleep(1)
"""
