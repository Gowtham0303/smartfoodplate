
import receive
import picamera
import sys
import time
import lcddisplay
import read_arduino
import Imageprocessing
import Nutrition
import authenticate
import RPi.GPIO as GPIO
import socket
import sys

UDP_IP = "10.0.0.44"

UDP_Port = 5015

sock = socket.socket(socket.AF_INET, # Internet

socket.SOCK_DGRAM) 
sock.bind((UDP_IP,UDP_Port))


GPIO.setmode(GPIO.BCM)
GPIO.setup(19,GPIO.IN)
tick=0
tock=0
flag=0
while(1):
    lcddisplay.Display()
    print 'Read the RFID '
    data, addr = sock.recvfrom(1024)
    rfid=receive.userid()
    rfid=data
   # print ("Rfid is",rfid)  
    tick=0
    flag=1

    while((rfid !='NoCard') and (tick<3000)and flag):
        print('processing data for a perticulat id',rfid)
        tick+=1
        if tock<1:
            username=authenticate.user(rfid)
        #print()
        if username=='NoUser':
            flag=0
            print 'flag',flag
            
        else:
            tock+=1
        
        lcddisplay.Username(username)
        #print ("Username is",username)
        if (GPIO.input(19)):
            w2=read_arduino.getweight()
            time.sleep(3)
            print ('The Weight is',w2)
            print 'capturing image'
            camera=picamera.PiCamera()
            camera.capture('imgcaptured.jpg')
            time.sleep(4)
            camera.close()
            print("Image has been captured")
            fid=Imageprocessing.processImage()
            print('fruit id is',fid)
            templist=Nutrition.getValues(fid)
            w=float(w2)*0.01
            fname=templist[0][0]
            c1=w*float(templist[0][1])
            c2=w*float(templist[0][2])
            c3=w*float(templist[0][3])
            c4=w*float(templist[0][4])
            lst=[]
            lst.append(c1)
            lst.append(c2)
            lst.append(c3)
            lst.append(c4)
            lcddisplay.fruitName(fname)
            lcddisplay.weight(w2)
            Nutrition.setConsumedValues(rfid,fid,c1,c2,c3,c4)
            lcddisplay.Nutrients(lst)
        else:
            lcddisplay.defaultDisplay()
finally:
        try:
            print("closing the port")
            sock.shutdown(1)
            sock.close()
	finally:
		sys.exit()
            

    
