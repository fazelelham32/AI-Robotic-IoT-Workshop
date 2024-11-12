#################################################
#########       Dr.Safieh Siadat        #########
#########       Danial Farajzade        #########
#########       Alireza Dadrass         #########
#################################################


import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

def High(channel):
        GPIO.output(channel, GPIO.HIGH)
def Low(channel):
        GPIO.output(channel, GPIO.LOW)
def Sleep(t):
        time.sleep(t)

def Blue():
        High(2)
        High(3)
        Sleep(0.3)
        High(4)
        Low(2)
        Sleep(0.3)
        High(17)
        Low(3)
        Sleep(0.3)
        Low(4)
        Sleep(0.3)
        Low(17)
        Sleep(0.3)

def All():
        High(2)
        Low(3)
        High(4)
        Low(17)
        High(22)
        Low(27)
        High(5)
        Low(6)

def LAll():
        Low(2)
        Low(3)
        Low(4)
        Low(17)
        Low(22)
        Low(27)
        Low(5)
        Low(6)

def Red():
        High(22)
        High(27)
        Sleep(0.3)
        High(5)
        Low(22)
        Sleep(0.3)
        High(6)
        Low(27)
        Sleep(0.3)
        Low(5)
        Sleep(0.3)
        Low(6)
        Sleep(0.3)

while True:
        Blue()
        Red()
        Sleep(0.5)
        All()
        Sleep(2.5)
