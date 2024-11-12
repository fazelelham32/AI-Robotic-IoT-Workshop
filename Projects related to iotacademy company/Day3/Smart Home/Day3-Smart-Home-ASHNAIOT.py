#################################################
#########           ASHNAIOT            #########
#################################################


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def High(channel):
        GPIO.output(channel, GPIO.HIGH)
def Low(channel):
        GPIO.output(channel, GPIO.LOW)
def Sleep(t):
        time.sleep(t)

def LEDOn():
    High(16)
    High(20)
    High(21)

def LEDOff():
    Low(16)
    Low(20)
    Low(21)

def FanOn():
    Low(12)

def FanOff():
    High(12)

def ReadMQ():
    print (GPIO.input(4))

while True:
    LEDOn()
    FanOff()
    ReadMQ()
    Sleep(3)
    LEDOff()
    FanOn()
    ReadMQ()
    Sleep(3)
 