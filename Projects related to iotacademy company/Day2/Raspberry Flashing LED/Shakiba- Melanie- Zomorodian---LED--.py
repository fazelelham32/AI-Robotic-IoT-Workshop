import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(3, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(4, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(5, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(6, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(19, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(26, GPIO.OUT, initial = GPIO.LOW)
while True:
	for i in [2,3,4,5]:
		GPIO.output(i, GPIO.HIGH)
	time.sleep(0.2)
	for i in [2,3,4,5]:
		GPIO.output(i, GPIO.LOW)
	time.sleep(0.2)
	for i in [6,13,19,26]:
		GPIO.output(i, GPIO.HIGH)
	time.sleep(0.2)
	for i in [6,13,19,26]:
		GPIO.output(i, GPIO.LOW)
	time.sleep(0.2)
		
	
		
	'''	GPIO.output(i, GPIO.LOW)
	GPIO.output(2, GPIO.HIGH)
	GPIO.output(3, GPIO.HIGH)
	GPIO.output(4, GPIO.HIGH)
	GPIO.output(5, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(2, GPIO.LOW)
	GPIO.output(3, GPIO.LOW)
	GPIO.output(4, GPIO.LOW)
	GPIO.output(5, GPIO.LOW)
	
	GPIO.output(26, GPIO.HIGH)
	GPIO.output(6, GPIO.HIGH)
	GPIO.output(13, GPIO.HIGH)
	GPIO.output(19, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(6, GPIO.LOW)
	GPIO.output(13, GPIO.LOW)
	GPIO.output(19, GPIO.LOW)
	GPIO.output(26, GPIO.LOW)'''
	
	for i in [2 , 6, 3, 13, 4, 19, 5, 26]:
		GPIO.output(i, GPIO.HIGH)
		time.sleep(0.1)
		GPIO.output(i, GPIO.LOW)
	for i in [26 , 5, 19, 4, 13, 3, 6, 2]:
		GPIO.output(i, GPIO.HIGH)
		time.sleep(0.1)
		GPIO.output(i, GPIO.LOW)
	
