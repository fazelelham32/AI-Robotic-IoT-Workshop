import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 


GPIO.setup(4,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(9,GPIO.OUT)
while True:
	GPIO.output(4, GPIO.HIGH)
	GPIO.output(3, GPIO.HIGH)
	GPIO.output(19, GPIO.HIGH) 
	GPIO.output(26, GPIO.HIGH)
	GPIO.output(6, GPIO.HIGH)
	GPIO.output(7, GPIO.HIGH)
	GPIO.output(8, GPIO.HIGH) 
	GPIO.output(9, GPIO.HIGH)   
	time.sleep(3)
	GPIO.output(4, GPIO.LOW)
	GPIO.output(3, GPIO.LOW)
	GPIO.output(19, GPIO.LOW)
	GPIO.output(26, GPIO.LOW)
	GPIO.output(6, GPIO.LOW)
	GPIO.output(7, GPIO.LOW)
	GPIO.output(8, GPIO.LOW)
	GPIO.output(9, GPIO.LOW)
	time.sleep(3)
		

	GPIO.output(3, GPIO.HIGH)
	GPIO.output(26, GPIO.HIGH)
	GPIO.output(7, GPIO.HIGH)
	GPIO.output(9, GPIO.HIGH)   
	time.sleep(3)
	GPIO.output(4, GPIO.HIGH)
	GPIO.output(3, GPIO.LOW)
	GPIO.output(19, GPIO.HIGH) 
	GPIO.output(26, GPIO.LOW)
	GPIO.output(6, GPIO.HIGH)
	GPIO.output(7, GPIO.LOW)
	GPIO.output(8, GPIO.HIGH) 
	GPIO.output(9, GPIO.LOW) 
	time.sleep(3)
	




