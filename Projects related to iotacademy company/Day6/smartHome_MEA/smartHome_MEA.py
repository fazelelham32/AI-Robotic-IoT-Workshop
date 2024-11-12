# Smart Home Automation v0.5 [MEA IoT Group]

import RPi.GPIO as GPIO
import time
import datetime
import requests
import json
import dht11
import paho.mqtt.client as paho
import MFRC522
import signal





mq2 = 4
fan = 12
leds = (16,20,21)
dht11pin = 26
servo = 19

dht11Instance = dht11.DHT11(pin=dht11pin)


actuatorsStatus = {'leds' : '', 'fan' : '', 'door' : '' }
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
        result = {'leds':req["feeds"][0]["field1"],'fan': req["feeds"][0]["field2"] , 'door' : req["feeds"][0]["field3"]}
        return result
        
        
# Write To Server

def writeStatus(status):

        channelKey = "N6B33OLZ39DYFUF8"
        url = "http://thingtalk.ir/update"
        
        req = requests.get(url, params={'key': channelKey, 'field1': status['mq2'], 'field2': status['temp'], 'field3': status['humidity']})



# Pins setup before main loop
setupGPIOs()


####################################################
# test funcions


p=GPIO.PWM(servo,50)

def go_backward():
        p.start(2.5)
def go_forward():
        p.start(6.0)


def setDoor(status):
        if(status == '1'):
                go_forward()
        else:
                go_backward()
                


        
##############################################

# RFID READER
userid =[197,209,30,195]
rfid =[1,1,1,1]

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print( "Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print ("Welcome to the MFRC522 data read example")
print( "Press Ctrl-C to stop.")

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
def continue_reading():
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print ("Card detected")
    
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        # Print UID
        print ("Card read UID: %s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3]))
        rfid[0] = uid[0]
        rfid[1] = uid[1]
        rfid[2] = uid[2]
        rfid[3] = uid[3]
    
        # This is the default key for authentication
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        
        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)

        # Authenticate
        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

        # Check if authenticated
        if status == MIFAREReader.MI_OK:
            MIFAREReader.MFRC522_Read(8)
            MIFAREReader.MFRC522_StopCrypto1()
        else:
            print ("Authentication error")


#####################################################################


# main loop
while True:
        continue_reading()
        
        actuatorsStatus = readStatus()


        print(actuatorsStatus)

        setLeds(actuatorsStatus['leds'])
        setFan(actuatorsStatus['fan'])

        sensorsStatus['mq2'] = readMQ2()

        readDht11()

        writeStatus(sensorsStatus)


        setDoor(actuatorsStatus['door'])
        print("rfid : " ,rfid)
        print("userid : " ,userid)
        if(userid == rfid):
                setDoor('0')
                time.sleep(2)
                
                setDoor('1')
                rfid=[0,0,0,0]
        else:
                setDoor('1')

        

        # just for test and will be functionalized soon
     #   if (int(sensorsStatus['temp']) >= 25):
     #           setFan('1')
    #    else:
   #             setFan('0')

   


        #p=GPIO.PWM(servo,50)
        #p.start(2)
        #p.stop()
        #p.start(6)



       # go_backward()
        #time.sleep(2)
        #go_forward()
        #time.sleep(2)

       
        
        #####################################################
        
        
        time.sleep(2)
        

        

        
                        
