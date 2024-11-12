# Smart Home Automation v0.4 [MEA IoT Group]

import RPi.GPIO as GPIO
import time
import requests
import json

mq2 = 4
fan = 12
leds = (16,20,21)
actuatorsStatus = {}
sensorsStatus = {}

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Setup GPIOs mode

def setupGPIOs():
	GPIO.setup(mq2,GPIO.IN)
	GPIO.setup(fan,GPIO.OUT)
	for led in leds:
	        GPIO.setup(led,GPIO.OUT)

	        
####################################################


# Actuators


def setLeds(status):
        counter = 0
        while counter < len(leds):
                GPIO.output(int(leds[counter]),int(status[counter]))

def setFan(status):
        GPIO.output(fan,int(status))
        
                
####################################################


# Sensors

def readMQ2():
        return GPIO.input(mq2)

####################################################


# Read from server

def readStatus():



        channelReadKey = "R3GG9XKV8Z9MJ10S"
        url = "http://thingtalk.ir/channels/666/feed.json"
        
        req = requests.get(url, params={'key': channelReadKey, 'results': '1'})
        req = req.json()
        result = {'leds':int(req["feeds"][0]["field1"]),'fan': int(req["feeds"][0]["field2"])}
        return result
        
        
# Write To Server

def writeStatus(status):

        channelKey = "N6B33OLZ39DYFUF8"
        url = "http://thingtalk.ir/update"
        
        req = requests.get(url, params={'key': channelReadKey, 'field1': status['mq2'])


####################################################


setupGPIOs()


while True:
        actuatorsStatus = readStatus()

        setLeds(actuatorsStatus['leds'])
        setFan(actuatorsStatus['fan'])

        sensorsStatus['mq2'] = readMQ2()

        writeStatus(sensorsStatus)

        time.sleep(1)
                        
