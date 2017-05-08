
import serial
import struct
def getweight():
	ser = serial.Serial('/dev/ttyACM0',9600)
	


	while True:

		read_serial=ser.readline()
		head=read_serial[0:2]
               # print(read_serial[0:2])
		data=read_serial[2:]
		if(head=="FF"):
			return str(int(str(data),16))

		
	


		
#print(getweight())

