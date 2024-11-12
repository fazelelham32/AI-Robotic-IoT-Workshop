import serial
import binascii
import xbee
serialport = serial.Serial("/dev/ttyUSB0" , baudrate = 38400 , timeout = 1)


print "uguyguyg"

sendData=["fd","8","00","00","11","22","33","4","1","2","3","4"]
serialport.write(xbee.prepare_sent_data(sendData))



while True:
    reciveData=xbee.getFromZigbee(zigbee=serialport)
