import cv2
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

while True:
    tStart=time.time()
    frame=picam2.capture_array()
    # Create a Region of Interest (ROI) frame
    ROI=frame[0:int(dispH/2),0:int(dispW/2)]
    frame[int(dispH/2):,int(dispW/2):] = ROI
    frame[:int(dispH/2),int(dispW/2):] = ROI
    frame[int(dispH/2):,:int(dispW/2)] = ROI
    cv2.putText(frame,str(int(fps))+' FPS',pos,font,height,myColor,weight)
    cv2.imshow("picam2",frame)
    cv2.imshow('ROI', ROI)
    if cv2.waitKey(1)==ord('q'):
        break
    tEnd=time.time()
    loopTime=tEnd-tStart
    fps=.9*fps +.1*(1/loopTime)
    #print(int(fps))
cv2.destroyAllWindows()