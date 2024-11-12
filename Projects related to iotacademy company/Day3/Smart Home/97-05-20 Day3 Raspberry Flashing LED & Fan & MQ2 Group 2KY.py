import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT) #LED 1
GPIO.setup(20,GPIO.OUT) #LED 2
GPIO.setup(21,GPIO.OUT) #LED 3
GPIO.setup(12,GPIO.OUT) # Fan
GPIO.setup(4,GPIO.IN)
def check_mq2():
	mq=GPIO.input(4)
	if (mq==True):
		print('OK')
	else:
		print("Alarm")

def led_turnon(): # Turn ON LEDs 
	GPIO.output(16,GPIO.HIGH)
	GPIO.output(20,GPIO.HIGH)
	GPIO.output(21,GPIO.HIGH)
	
	
def led_turnoff(): # Turn OFF LEDs 
	GPIO.output(16,GPIO.LOW)
	GPIO.output(20,GPIO.LOW)
	GPIO.output(21,GPIO.LOW)
	
	
def fan_turnon(): # Turn On FAN
	GPIO.output(12,GPIO.HIGH)
	
def fan_turnoff(): #Turn Off Fan
	GPIO.output(12,GPIO.LOW)
while True:
	check_mq2()
	led_turnon() 
	time.sleep(3) # Turn ON LEDs for 3 sec
	led_turnoff()
	time.sleep(3) # Turn OFF LEDs for 3 sec
	fan_turnon()
	time.sleep(3) # Turn ON Fan for 3 sec
	fan_turnoff()
	time.sleep(3) # Turn OFF Fan for 3 sec
	
	

	
