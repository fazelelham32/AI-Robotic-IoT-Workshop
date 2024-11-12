import RPi.GPIO as GPIO
import time
import requests
import json
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(4,GPIO.IN)

def relay_off():
	GPIO.output(12,GPIO.HIGH)
def relay_on():
	GPIO.output(12,GPIO.LOW)
def mq2():
	a=GPIO.input(4)
	return a
def high(i):
	GPIO.output(i,GPIO.HIGH)
def low1(i):
	GPIO.output(i,GPIO.LOW)

def write1(i):
	f=requests.get(i)
	return f
def read1(i):
	f=requests.get(i)
	data=json.loads(f.text)['feeds'][0]
	return data 
	
	
while(True):
	data=read1("http://thingtalk.ir/channels/660/feed.json?key=VFD44N3X2E8SDSN7&results=1")
	led=int(data['field1'])
	fan1=int(data['field2'])
	a=mq2()
	s=write1("http://thingtalk.ir/update?key=VFD44N3X2E8SDSN7&field3="+str(a)+"&field1="+str(led)+"&field2="+str(fan1))
	if led ==1:
		high(16)
		time.sleep(0.3)
		low1(16)
		time.sleep(0.3)
	if led==0:
		low1(16)
	if fan1==1:
		relay_off()
	if fan1==0:
		relay_on()
	

	
	
	
	
