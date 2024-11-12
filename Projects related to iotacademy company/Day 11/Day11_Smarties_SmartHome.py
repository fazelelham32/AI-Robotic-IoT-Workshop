import RPi.GPIO as GPIO
from time import sleep
import json
import urllib2
import requests
import dht11
import time
import datetime
import os
import MFRC522
import signal
import paho.mqtt.client as paho
import ADS1118
import typek
#from mq import *

#GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# setup GPIOs OUT
for i in [16,20,21,12,19]:
	GPIO.setup(i,GPIO.OUT, initial=GPIO.LOW)

# setup GPIOs IN
for i in [4,13]:
	GPIO.setup(i,GPIO.IN)

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()
    
# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
def readUID():
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print "Card detected"
    
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        # Print UID
        UID = "%s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3])
        print ("Card read UID: %s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3]))
    
        # This is the default key for authentication
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        
        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)

        # Authenticate
        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

        # Check if authenticated
        if  status == MIFAREReader.MI_OK:
			MIFAREReader.MFRC522_Read(8)
			MIFAREReader.MFRC522_StopCrypto1()
			return UID
        else:
            print ("Authentication error")

# read data using pin 14
instance = dht11.DHT11(pin=26)


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

# read from mq2 sensor
def mq2_read() :
	data=GPIO.input(4)
	return (data)

#turn on fan
def fan_on():
	GPIO.output(12,GPIO.LOW)

#turn off fan
def fan_off():
	GPIO.output(12,GPIO.HIGH)

def on_message(client, userdata, msg):
	print(str(msg.payload))
	if str(msg.payload)=='open' :
		go_backwards()
		time.sleep(2)
		go_forward()
		

def write_server(led,fan,mq2,temp,humidity,door):
	url="http://thingtalk.ir/update?key=17F82B8WX1YAD6OO&field1={0}&field2={1}&field3={2},&field4={3},&field5={4}&field6={5}".format(led,fan,mq2,temp,humidity,door)
	requests.get(url)


def read_server():
	url = 'http://thingtalk.ir/channels/637/feed.json?key=17F82B8WX1YAD6OO&results=1'
	data = json.load(urllib2.urlopen(url))
	if len(data['feeds']) ==0:
		print ("IndexError:no data in feeds")
	else:
		led = data['feeds'][0]['field1']
		fan = data['feeds'][0]['field2']
		mq2 = data['feeds'][0]['field3']
		temp = data['feeds'][0]['field4']
		humidity = data['feeds'][0]['field5']
		door = data['feeds'][0]['field6']
		return led,fan,mq2,temp,humidity,door
				
	return (0,0,0,0,0,0)
	
# using servo for motor
p = GPIO.PWM(19,50)
def go_backwards():
	p.start(2.5)
def go_forward():
	p.stop()
	p.start(7)


client=paho.Client()
client.on_message = on_message
client.connect("thingtalk.ir",1883)
client.subscribe("smarties",qos=1)
client.loop_start()
#int_gas = ADS1118.encode(single_shot=True, temp_sensor=True, data_rate=5)
#tc = ADS1118.encode(single_shot=True, multiplex=4, gain=1, data_rate=5)
#ads = ADS1118.ADS1118(SCLK=17, DIN=22, DOUT=27) # set the GPIO pins
#M=MQ()
while True:
	
	UID = readUID()
	print(UID)
	if UID == '32,157,124,25' or UID=='181,161,94,190':
		go_backwards()
		client.publish("smarties","door is opened",qos=1)
		time.sleep(2)
		go_forward()
		client.publish("smarties","door is closed",qos=1)
		
	mq2 = mq2_read()
	if mq2==False:
		client.publish("smarties","smoke detected",qos=1)
	
	print(mq2)
	
	ledStatus,fanStatus,mq2Status, tempStatus, humidityStatus, doorStatus = read_server()
	

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
		
	
	flag = True	
	if fanStatus == '1':
		fan_on()
		flag = False
	if fanStatus == '0':
		fan_off()
		flag = False
	if fanStatus=='a':
		flag = True
		
	if doorStatus == '1':
		go_backwards()
		client.publish("smarties","door is opened",qos=1)
		time.sleep(2)
		
	if doorStatus == '0':
		go_forward()
		client.publish("smarties","door is closed",qos=1)
		#time.sleep(2)
		
	if GPIO.input(13)==True:
		client.publish("smarties","movement detected",qos=1)
		led_on([16],0)
		led_off([20],0)
		led_off([21],0)
	if GPIO.input(13)==False :
		ledStatus=ledStatus
		
	result=instance.read()
	if result.is_valid():
		print("Last valid input: " + str(datetime.datetime.now()))
		print("Temperature: %d C" % result.temperature)
		print("Humidity: %d %%" % result.humidity)	
	
		if result.temperature>20 and flag:
			fan_on()
		elif result.temperature<20 and flag:
			fan_off()
		
	
	'''try:
		print("Press CTRL+C to abort.")   
		print ("*****************************") 
		perc = mq.MQPercentage()#read MQ2 data
		sys.stdout.write("\r")
		sys.stdout.write("\033[K")
		sys.stdout.write("LPG: %g ppm, CO: %g ppm, Smoke: %g ppm" % (perc["GAS_LPG"]*1000, perc["CO"]*1000, perc["SMOKE"]*1000))
		r = requests.get('http://thingtalk.ir/update?key=17F82B8WX1YAD6OO&field1=' + ledStatus+'&field2='+fanStatus+'&field3='+mq+'&field4='+str(result.temperature) + '&field5=' + str(result.humidity)+ '&field6=' +doorStatus+ '&field7=' +str(perc["CO"]*1000)+ '&field8=' +str(perc["SMOKE"]*1000))##write MQ2 data to server
		sys.stdout.flush()
		time.sleep(2)
	except:
		print("\nAbort by user")'''
	write_server(ledStatus,fanStatus,mq2,result.temperature,str(result.humidity),doorStatus)



		
