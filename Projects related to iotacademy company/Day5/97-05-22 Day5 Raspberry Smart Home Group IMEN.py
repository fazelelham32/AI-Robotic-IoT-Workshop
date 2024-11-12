import RPi.GPIO as GPIO
import time
import datetime
import requests
import json
import dht11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(16,GPIO.OUT) #LED 1
GPIO.setup(20,GPIO.OUT) #LED 2
GPIO.setup(21,GPIO.OUT) #LED 3
GPIO.setup(12,GPIO.OUT) # Fan
GPIO.setup(4,GPIO.IN) # MQ2

# read data using pin 26
instance = dht11.DHT11(pin=26) # DHT11

def readdata():
	request = requests.get ('http://thingtalk.ir/channels/656/feed.json?key=STM902H7RN2XO65Y&results=1')
	data=json.loads(request.text)['feeds'][0]
	return data

def check_dht11():
	result = instance.read()
	if result.is_valid():
		print("Last valid input: " + str(datetime.datetime.now()))
		print("Temperature: %d C" % result.temperature)
		print("Humidity: %d %%" % result.humidity)
		time.sleep(2)
	return result

def check_mq2():
	mq=GPIO.input(4)
	return mq
	'''if (mq==True):
		print('OK')
	else:
		print("Alarm")'''

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
    
	data=readdata()
	led=data['field1']
	fan=data['field2']
	
	if led=="1" :
		led_turnon()
	else:
		led_turnoff()
	
	if fan=="1":
		fan_turnon()
	else:
		fan_turnoff()
	
	mq = check_mq2()
	result=check_dht11()
	if result.is_valid():
		temperature = result.temperature
		humidity = result.humidity
		if temperature >= 30 :
			fan_turnon ()
		else:
			fan_turnoff ()
		
	q = requests.post ('http://thingtalk.ir/update?key=STM902H7RN2XO65Y&field1='+str(led)+'&field2='+str(fan)+'&field3='+str(mq)+'&field4='+str(temperature)+'&field5='+str(humidity))

			
	

	
