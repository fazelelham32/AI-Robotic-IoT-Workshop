import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


'''
GPIO.output(16,GPIO.HIGH)
GPIO.output(20,GPIO.HIGH)
GPIO.output(21,GPIO.HIGH)
'''

GPIO.setup(4,GPIO.IN)

for i in [16,20,21,12]:
	GPIO.setup(i,GPIO.OUT, initial=GPIO.LOW)
	

def led_off(led,delay):
	for i in led:
		GPIO.output(i,GPIO.LOW)
	sleep(delay)
	

def led_on(led,delay):
	for i in led:
		GPIO.output(i,GPIO.HIGH)
	sleep(delay)
	
def check_mq2() :
	mq=GPIO.input(4)
	if (mq==False):
		print ("alarm")



while True:
	led_on([16,20,21],3)
	led_off([16,20,21],3)
	GPIO.output(12,GPIO.HIGH)
	sleep(5)
	GPIO.output(12,GPIO.LOW)
	sleep(5)
	check_mq2()