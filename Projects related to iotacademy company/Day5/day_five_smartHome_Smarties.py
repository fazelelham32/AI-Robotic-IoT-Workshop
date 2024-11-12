import RPi.GPIO as GPIO
from time import sleep
import json
import urllib2
import requests
import dht11
import time
import datetime
import os

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# read data using pin 14
instance = dht11.DHT11(pin=26)

# setup GPIOs OUT
for i in [16,20,21,12,19]:
	GPIO.setup(i,GPIO.OUT, initial=GPIO.LOW)

# setup GPIOs IN
for i in [4]:
	GPIO.setup(i,GPIO.IN)

# turn on LEDs
def led_on(led,delay):
	for i in led:
		GPIO.output(i,GPIO.HIGH)
	sleep(delay)

# turn off LEDs
def led_off(led,delay):
	for i in led:
		GPIO.output(i,GPIO.LOW)
	sleep(delay)

# reed from mq2 sensor
def mq2_read() :
	data=GPIO.input(4)
	return (data)

#turn on fan
def fan_on():
	GPIO.output(12,GPIO.LOW)

#turn off fan
def fan_off():
	GPIO.output(12,GPIO.HIGH)


def write_server(led,fan,mq2,temp,humidity):
	url="http://thingtalk.ir/update?key=17F82B8WX1YAD6OO&field1={0}&field2={1}&field3={2},&field4={3},&field5={4}".format(led,fan,mq2,temp,humidity)
	requests.get(url)


def read_server():
	url = 'http://thingtalk.ir/channels/637/feed.json?key=17F82B8WX1YAD6OO&results=1'
	data = json.load(urllib2.urlopen(url))
	print(data["feeds"])
	if len(data['feeds']) ==0:
		print ("IndexError:no data in feeds")
	else:
		led = data['feeds'][0]['field1']
		fan = data['feeds'][0]['field2']
		mq2 = data['feeds'][0]['field3']
		temp = data['feeds'][0]['field4']
		humidity = data['feeds'][0]['field5']
		return led,fan,mq2,temp,humidity
		
		
	#print (data)
	return (0,0,0,0,0)
	
########################

p = GPIO.PWM(19,50)

def go_backwards():
	p.start(2.5)
	
def go_forward():
	p.stop()
	p.start(6)
	
go_backwards()
time.sleep(2)
go_forward()
time.sleep(2)

########################

while True:
	mq2 = mq2_read()
	#print(mq2)

	ledStatus,fanStatus,mq2Status, tempStatus, humidityStatus = read_server()

	print (str(ledStatus))
	if ledStatus=='1':
		led_on([16],0)
		led_off([20],0)
		led_off([21],0)
		
	elif ledStatus=='2':
		led_on([20],0)
		led_off([16],0)
		led_off([21],0)
		
	elif ledStatus=='3':
		led_on([21],0)
		led_off([16],0)
		led_off([20],0)
		
	elif ledStatus=='0':
		led_off([16,20,21],0)
		
	if fanStatus == '10':
		fan_on()
	if fanStatus == '-10':
		fan_off()
		
#################################
	
	result = instance.read()
	print("result.temperature= " + str(result.temperature))
	if result.is_valid():
		print("Last valid input: " + str(datetime.datetime.now()))
		print("Temperature: %d C" % result.temperature)
		print("Humidity: %d %%" % result.humidity)
		
		if result.temperature>20:
			fan_on()
		else:
			fan_off()
		
		write_server(3,1,1,result.temperature,result.humidity)
	time.sleep(1)


