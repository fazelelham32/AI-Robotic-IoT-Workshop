import binascii

import serial

import time


def xbee_byte_to_str(byte):
    #return byte
    return str(binascii.hexlify(byte))


def xbee_byte_to_int(byte):
    print "b :" + byte
    return int(xbee_byte_to_str(byte), 16)
    

def prepare_sent_data(sendData):
	returnData = [0]*len(sendData)
	i = 0
	while i < len(sendData):
		returnData[i] = int(sendData[i], 16)
		i=i+1
	returnData = binascii.hexlify(bytearray(returnData))
	returnData = bytearray.fromhex(returnData)
	return returnData


def getFromZigbee(zigbee, dataLength=8):
	print "waiting for zigbee"
	returnData=['ff'] * dataLength
	while True:
		recievedData = zigbee.read()
		if recievedData == '':
			return
		pureData = str(binascii.hexlify(recievedData))
		print("recievedData= " + str(pureData))
		if pureData == "fd":#FD
			returnData[0] = pureData
			break
	i = 1
	while i < dataLength:
		recievedData = zigbee.read()
		if recievedData == '':
			continue
		data = str(binascii.hexlify(recievedData))
		returnData[i] = data
		i+=1
	print "returnData:" + str(returnData)
	print "data recieved"
	return returnData

class XBeeModule:
    def __init__(self, serial_dir, baudrate, timeout, module_name, address):
        self.name = module_name
        self.address = address
        self.serial_dir = serial_dir
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_port = serial.Serial(self.serial_dir, baudrate=self.baudrate, timeout=self.timeout)

    def get_str_byte(self):
        received_byte = self.serial_port.read()
        #print "received_byte:" + received_byte
        return xbee_byte_to_str(received_byte)

    def get_int_byte(self):
        received_byte = self.serial_port.read()
        print received_byte
        return xbee_byte_to_int(received_byte)

    def send_data(self, xbee_data):
        """ **Sends data according to the XBee format:** \n
            BYTE 1: FD if sending to a specific destination, something else if not \n
            BYTE 2: # of data bytes to send \n
            BYTE 3 and 4: destination address \n
            OTHER BYTES: actual data \n
            **EXAMPLE:** data = [0xfd, 0x02, 0x00, 0x01, 0xa1, 0xb2] sends the TWO numbers: 0xa1 and 0xb2
            to XBee module in the network with address 0x0001...
        """
        self.serial_port.write(xbee_data.prepare_to_send())
        print "COMMANDS SENT!"

    def receive_data(self):
        print "recive data started"
        data = XBeeData(single_dest=True, nums_count=0, dest_address="", origin_address="", nums=[])
        while True:
            byte = self.get_str_byte()
            #print type(byte)
            #print "Byte: " + str(byte)
            if byte == "fd":
                data.single_dest = True
                data.nums_count = self.get_int_byte()
                data.dest_address = self.address 
                dummy1, dummy2 = (self.get_int_byte(), self.get_int_byte())
                for i in range(data.nums_count):
					#temp=self.get_int_byte()
					#print "temp" +str(temp)
					#data.nums.append(temp)
					data.nums.append(self.get_int_byte())
                
                data.origin_address = self.get_str_byte() + self.get_str_byte()
                return data

class XBeeData:
    """ **This class defines the data format required in a XBee network** \n
        **single_dest:** True if data is sent to a specific destination \n
        **data_count** # of data bytes (numbers) to be sent \n
        **data:** an array of hex numbers to be sent e.g. [0x01, 0x02, ...]
    """

    def __init__(self, single_dest, nums_count, dest_address, origin_address, nums):
        self.single_dest = single_dest
        self.nums_count = nums_count
        self.nums = nums
        self.dest_address = dest_address
        self.origin_address = origin_address

    def prepare_to_send(self):
        """Returns an array which is ready to be sent using a XBeeModule obj"""
        result = []

        if self.single_dest:
            result.append(253)  # 0xfd = 253
        else:
            result.append(200)

        result.append(self.nums_count)
        result.append(int(self.dest_address[:2], 16))
        result.append(int(self.dest_address[2:], 16))

        for num in self.nums:
            result.append(num)

        result = binascii.hexlify(bytearray(result))
        result = bytearray.fromhex(result)
        return result


    def print_data(self):
        if len(self.nums) == 0:
            return

        print "***DATA:"
        if self.single_dest:
            print "First byte: fd"
        else:
            print "First byte: fc"
        print "Destination: " + self.dest_address
        print "Origin: " + self.origin_address
        print "Number of bytes: " + str(self.nums_count)
        print "Data: " + str(self.nums)
        print ""
