#################################################
#########           ASHNAIOT            #########
#################################################


import RPi.GPIO as GPIO
import time
import requests

import dht11

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

instance = dht11.DHT11(pin = 26)
def DHTRead():
    result = instance.read()

    if result.is_valid():
        return [result.humidity,result.temperature]
    else:
        print("Error: %d" % result.error_code)
        return ['E','E']

def High(channel):
        GPIO.output(channel, GPIO.HIGH)
def Low(channel):
        GPIO.output(channel, GPIO.LOW)
def Sleep(t):
        time.sleep(t)

def ROn():
    High(20)


def GOn():
    High(16)

def BOn():
    High(21)


def ROff():
    Low(20)

def GOff():
    Low(16)

def BOff():
    Low(21)


def FanOn():
    Low(12)

def FanOff():
    High(12)

def ReadMQ():
    return GPIO.input(4)

def GetFan():
    r = requests.get('http://thingtalk.ir/channels/640/feed.json?key=U5RSR6TJ6KIWA010&results=1').json()
    return r['feeds'][0]['field2']
def GetLED():
    r = requests.get('http://thingtalk.ir/channels/640/feed.json?key=U5RSR6TJ6KIWA010&results=1').json()
    return r['feeds'][0]['field1']

while True:
    getFan=GetFan()
    if getFan=='1':
        FanOn()
    else:
        FanOff()
    getLED=GetLED()
    if getLED=='000':
        ROff()
        GOff()
        BOff()
    elif getLED=='100':
        ROn()
        GOff()
        BOff()
    elif getLED=='010':
        ROff()
        GOn()
        BOff()
    elif getLED=='001':
        ROff()
        GOff()
        BOn()
    dh = DHTRead()
    mq1=ReadMQ()
    uri='http://thingtalk.ir/update?key=U5RSR6TJ6KIWA010&field1=%s&field2=%s&field3=%s&field4=%s&field5=%s'%(getLED,getFan,mq1,dh[1],dh[0])
    print(uri)
    r = requests.get(uri)
    print('MQ Val: %s, Ressponse: %s'%(mq1,r))
    Sleep(3)

