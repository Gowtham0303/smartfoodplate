import socket
import sys
def userid():
    UDP_IP = "10.0.0.44"

    UDP_Port = 5015

    sock = socket.socket(socket.AF_INET, # Internet

    socket.SOCK_DGRAM) 
    sock.bind((UDP_IP,UDP_Port))
    try:
        print('entered into try')
        while True:
            data, addr = sock.recvfrom(1024)
            print("data from rfid", data)
            return data
	#print ("received message:" (data))
    finally:
        try:
            print("closing the port")
            sock.shutdown(1)
            sock.close()
	finally:
		sys.exit()
userid()
