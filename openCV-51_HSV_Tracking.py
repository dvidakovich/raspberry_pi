# Create an Opencv mask that focuses on a target
# hue, saturation & value range to track objects

import cv2
import numpy as np
from picamera2 import Picamera2
import time
picam2=Picamera2()
dispW = 1280
dispH = 720
picam2.preview_configuration.main.size=(dispW,dispH)
picam2.preview_configuration.main.format="RGB888"
picam2.preview_configuration.controls.FrameRate=30
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()
fps=0
pos=(30,60)
font=cv2.FONT_HERSHEY_SIMPLEX
height=1.5
myColor=(0,0,255)
weight=3

# Create min and max hue, saturation & value variables to track objects
hueLow = 160
hueHigh = 179

satLow = 100
satHigh = 255

valLow = 100
valHigh = 255

# Create a lower bound array using numpy
lowerBound = np.array([hueLow, satLow, valLow])

# Create an upper bound array using numpy
upperBound = np.array([hueHigh, satHigh, valHigh])


while True:
    tStart=time.time()
    frame=picam2.capture_array()
    # Create an HSV frame
    frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    # Create a mask for pixels not in range
    myMask = cv2.inRange(frameHSV,lowerBound, upperBound)

    # Create a small frame to show the mask
    myMaskSmall = cv2.resize(myMask,(int(dispW/2),int(dispH/2)))

    # Create special frame of object of interest
    objectOfInterest = cv2.bitwise_and(frame,frame,mask=myMask)

    # Make the object of interest small
    objectOfInterestSmall = cv2.resize(objectOfInterest,(int(dispW/2),int(dispH/2)))

    # Print the HSV frame values
    print(frameHSV[int(dispH/2),int(dispW/2)])
    # Create a frame for FPS
    cv2.putText(frame,str(int(fps))+' FPS',pos,font,height,myColor,weight)
    #Show the frame
    cv2.imshow("picam2",frame)

    # Show the mask frame
    cv2.imshow('My Mask',myMaskSmall)

    # Show the small object of interest
    cv2.imshow('Object of Interest', objectOfInterestSmall)

    # Create an if statement to break the loop
    if cv2.waitKey(1)==ord('q'):
        break
    # Calculate the FPS
    tEnd=time.time()
    loopTime=tEnd-tStart
    fps=.9*fps +.1*(1/loopTime)
cv2.destroyAllWindows()