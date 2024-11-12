# Smart Home Automation v0.5 [MEA IoT Group]

import RPi.GPIO as GPIO
import time
import datetime
import requests
import json
import dht11
import paho.mqtt.client as paho



mq2 = 4
fan = 12
leds = (16,20,21)
dht11pin = 26
servo = 19

dht11Instance = dht11.DHT11(pin=dht11pin)


actuatorsStatus = {'leds' : '', 'fan' : ''}
sensorsStatus = {'mq2' : '' , 'temp' : '' , 'humidity': ''}

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Setup GPIOs mode

def setupGPIOs():
	GPIO.setup(mq2,GPIO.IN)
	GPIO.setup(fan,GPIO.OUT)
	GPIO.setup(servo,GPIO.OUT)
	for led in leds:
	        GPIO.setup(led,GPIO.OUT)

	        
####################################################


# Actuators


def setLeds(status):
        counter = 0
        ledstat = str(status)
        while counter < len(leds):
                if(ledstat[counter] == '1'):                
                        GPIO.output(leds[counter],GPIO.HIGH)
                else:
                        GPIO.output(leds[counter],GPIO.LOW)
                counter += 1

def setFan(status):
        if(status == '0'):
                GPIO.output(fan,GPIO.HIGH)
        else:
                GPIO.output(fan,GPIO.LOW)


        
                
####################################################


# Sensors

def readMQ2():
        return GPIO.input(mq2)

def readDht11():
        result = dht11Instance.read()
        if result.is_valid():
               # print("Last valid input: " + str(datetime.datetime.now()))
               sensorsStatus['temp'] = result.temperature
               sensorsStatus['humidity'] = result.humidity
               print("Temperature: ", sensorsStatus['temp'])
               print("Humidity: ", sensorsStatus['humidity'])

        

####################################################


# Read from server

def readStatus():

        channelReadKey = "R3GG9XKV8Z9MJ10S"
        url = "http://thingtalk.ir/channels/666/feed.json"
        
        req = requests.get(url, params={'key': channelReadKey, 'results': '1'})
        req = req.json()
        result = {'leds':req["feeds"][0]["field1"],'fan': req["feeds"][0]["field2"]}
        return result
        
        
# Write To Server

def writeStatus(status):

        channelKey = "N6B33OLZ39DYFUF8"
        url = "http://thingtalk.ir/update"
        
        req = requests.get(url, params={'key': channelKey, 'field1': status['mq2'], 'field2': status['temp'], 'field3': status['humidity']})


####################################################


# Pins setup before main loop
setupGPIOs()


# main loop
while True:
        
        actuatorsStatus = readStatus()


        print(actuatorsStatus)

        setLeds(actuatorsStatus['leds'])
        setFan(actuatorsStatus['fan'])

        sensorsStatus['mq2'] = readMQ2()

        readDht11()

        writeStatus(sensorsStatus)


        # just for test and will be functionalized soon
        if (int(sensorsStatus['temp']) >= 25):
                setFan('1')
        else:
                setFan('0')
                        


        p=GPIO.PWM(servo,50)
        #p.start(2)
        #p.stop()
        #p.start(6)
        #####################################################
        
        
        time.sleep(2)
        

        

        
                        
