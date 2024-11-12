import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(4,GPIO.IN)

def led_turnon():
	GPIO.output(16,GPIO.HIGH)
	GPIO.output(20,GPIO.HIGH)
	GPIO.output(21,GPIO.HIGH)

def led_turnoff():
	GPIO.output(16,GPIO.LOW)
	GPIO.output(20,GPIO.LOW)
	GPIO.output(21,GPIO.LOW)

def fan_turnon():
	GPIO.output(12,GPIO.LOW)

def fan_turnoff():
	GPIO.output(12,GPIO.HIGH)

def MQ2_sensor():
	if GPIO.input(4):
		print("safe")
	else:
		print("Warning!")
	
while True:
	led_turnon()
	time.sleep(1)
	led_turnoff()
	time.sleep(1)
	fan_turnoff()
	MQ2_sensor()
