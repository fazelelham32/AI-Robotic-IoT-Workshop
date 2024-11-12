import RPi.GPIO as GPIO
import time
import requests
import json
import dht11
import datetime
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(4,GPIO.IN)
instance = dht11.DHT11(pin=26)

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
	return GPIO.input(4)
	
def temp_humid():
	result=instance.read()
	print (result)
	return result
	
def read_data():
	req = requests.get('http://thingtalk.ir/channels/661/feed.json?key=CYC0SANLFK770CZX&results=1')
	data=json.loads(req.text)['feeds'][0]
	return data
	
def check_temp(t):
	if t>=25:
		fan_turnon()
		print("turn onnnnnnnnnnnnnnnnnnnn")
	
p=GPIO.PWM(19,50)

def go_backward():
	p.start(1.0)
	
def go_forward():
	p.stop()
	p.start(6.0)

go_backward()
time.sleep(2)
go_forward()
time.sleep(2)
	
while True:
	data=read_data()
	#print (data)
	led=data['field1']
	fan=data['field2']
	#print(led)
	#print(fan)
	if led=='1':
		led_turnoff()
	else:
		led_turnon()
		
		
	#if fan=='1':
		#fan_turnoff()
	#else:
		#fan_turnon()
	
	mq2=MQ2_sensor()
	print mq2
	#req = requests.get("http://thingtalk.ir/update?key=CYC0SANLFK770CZX&field1="+str(led)+"&field2="+str(fan)+"&field3="+str(mq2))
	#print(req)
	
	result=temp_humid()
	if result.is_valid():
		temp=result.temperature
		humid=result.humidity
		req = requests.get("http://thingtalk.ir/update?key=CYC0SANLFK770CZX&field1="+str(led)+"&field2="+str(fan)+"&field3="+str(mq2)+"&field4="+str(temp)+"&field5="+str(humid))	
		time.sleep(1)
		print("temp",temp)
		print("humid",humid)
		temp1=int(data['field4'])
		check_temp(temp1)

		
		
    
