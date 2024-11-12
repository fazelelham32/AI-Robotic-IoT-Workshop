
import RPi.GPIO as GPIO
import requests
import json
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


GPIO.setup(4,GPIO.IN)


for i in [16,20,21,12]:
	GPIO.setup(i,GPIO.OUT, initial=GPIO.LOW)
	

def led_off():
	for i in [16,20,21]:
		GPIO.output(i,GPIO.LOW)
	
	

def led_on(led,delay):
	for i in led:
		GPIO.output(i,GPIO.HIGH)
	sleep(delay)
	
def led_rgb_red():
		GPIO.output(16, GPIO.HIGH)
		'''sleep(3)
		GPIO.output(16, GPIO.LOW)'''
		
def led_rgb_blue():
		GPIO.output(20, GPIO.HIGH)
		'''sleep(3)
		GPIO.output(20, GPIO.LOW)'''
		
def led_rgb_green():
		GPIO.output(21, GPIO.HIGH)
		'''sleep(3)
		GPIO.output(21, GPIO.LOW)'''				
	
def check_mq2() :
	return GPIO.input(4)
	

def read_server(field):
	r = requests.get ("http://thingtalk.ir/channels/658/feed.json?key=J7DA72R8BHBZU4QK&results=1")
	x = json.loads(r.text)['feeds'][0]
	y = x [field]
	return y
	


		
	

while True:

	'''led_on([16,20,21],3)
	led_off([16,20,21],3)
	GPIO.output(12,GPIO.HIGH)
	sleep(5)
	GPIO.output(12,GPIO.LOW)
	sleep(5)
	check_mq2()
	led_rgb_red()
	led_rgb_blue()
	led_rgb_green()'''
	led=read_server('field1')
	fan=read_server('field2')
	fire=check_mq2()
	#print(led)
	print(fan)
	if led=="1":
		led_rgb_red()
	elif led=="2":
		led_rgb_blue()
	elif led=="3":
		led_rgb_green()
	elif led=="0":
		led_off()
	if fan=="0":
		GPIO.output(12,GPIO.HIGH)
	elif fan=="1":
		GPIO.output(12,GPIO.LOW)
		
	mq2 = check_mq2()
	print(mq2)
	r=requests.get('http://thingtalk.ir/update?key=J7DA72R8BHBZU4QK&field1='+ led +'&field2='+ fan +'&field3=' + str(mq2))
	print(r)
	
	sleep(5)
	
	
	
