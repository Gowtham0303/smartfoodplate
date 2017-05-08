import cv2
import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg

def IdentifyContourArea(mask):
    kern_dilate = np.ones((1,1),np.uint8)
    kern_erode = np.ones((3,3),np.uint8)
    mask=cv2.erode(mask,kern_erode)
    mask=cv2.dilate(mask,kern_dilate)
    contours,hierarchy=cv2.findContours(mask,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    area=[0]
    for i in range(len(contours)):
        area.append(cv2.contourArea(contours[i]))
    return max(area)  

def greenLimits():
    lower_limit=np.array([17,59,33])
    upper_limit = np.array([44,190,149])
    return lower_limit,upper_limit

def redLimits():
    lower_limit=np.array([155,98,78])
    upper_limit = np.array([180,255,255])
    return lower_limit,upper_limit

def orangeLimits():
    lower_limit=np.array([5,102,108])
    upper_limit = np.array([16,248,215])
    return lower_limit,upper_limit

def yellowLimits():
    lower_limit=np.array([9,101,104])
    upper_limit = np.array([23,178,253])
    return lower_limit,upper_limit

def processImage():
    print 'entered image processing '
    fid=0
    frame = cv2.imread('imgcaptured.jpg')
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    for c in range(3):
        if c==0:
            lower_limit,upper_limit=greenLimits()
            mask=cv2.inRange(hsv,lower_limit,upper_limit)
            area=IdentifyContourArea(mask)
            if area>5000:
                fid=int(1000)
                print("Green fid :1000")
                break
                
        elif c==1:
            lower_limit,upper_limit=redLimits()
            mask=cv2.inRange(hsv,lower_limit,upper_limit)
            area=IdentifyContourArea(mask)
            if area>5000:
                fid=int(1001)
                print("red fid :1001")
                break
        elif c==2:
            lower_limit,upper_limit=orangeLimits()
            mask=cv2.inRange(hsv,lower_limit,upper_limit)
            area=IdentifyContourArea(mask)
            if area>5000:
                fid=int(1002)
                print("orange fid :1002")
                break
        elif c==3:
            lower_limit,upper_limit=yellowLimits()
            mask=cv2.inRange(hsv,lower_limit,upper_limit)
            area=IdentifyContourArea(mask)
            if area>5000:
                fid=int(1003)
                print("yellow fid :1003")
                break
        
        
        else:
         	print('No image found')
         	fid=int(0000)
    x=fid
    return x
    

