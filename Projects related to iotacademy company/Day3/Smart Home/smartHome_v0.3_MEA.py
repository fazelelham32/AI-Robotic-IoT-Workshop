# Smart Home Automation v0.3 [MEA IoT Group]

import RPi.GPIO as GPIO
import time

mq2 = 4
fan = 12
leds = (16,20,21)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Setup GPIOs mode

def setupGPIOs():
	GPIO.setup(mq2,GPIO.IN)
	GPIO.setup(fan,GPIO.OUT)
	for led in leds:
	        GPIO.setup(led,GPIO.OUT)
'''	
def setupMQ2():
	GPIO.setup(mq2,GPIO.IN)

def setupFan():
	GPIO.setup(fan,GPIO.OUT)

def setupLeds():
    for led in leds:
        GPIO.setup(led,GPIO.OUT)
'''

####################################################


# Actuators

def ledsOn():
	for led in leds:
		GPIO.output(led,GPIO.HIGH)

def ledsOff():
	for led in leds:
		GPIO.output(led,GPIO.LOW)

def fanOn():
	GPIO.output(fan,GPIO.LOW)

def fanOff():
	GPIO.output(fan,GPIO.HIGH)

####################################################


# Sensors

def readMQ2():
        return GPIO.input(mq2)

####################################################

setupGPIOs()
ledsOn()
fanOn()
time.sleep(3)
ledsOff()
fanOff()

while True:
	print ("MQ2 :",readMQ2())
		
