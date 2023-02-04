import cv2
from picamera2 import Picamera2
import time
picam2=Picamera2()
picam2.preview_configuration.main.size=(640,360)
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

upperLeft=(250,50)
lowerRight=(350,125)
rColor=(255,0,255)
thickness=7

cent=(145,245)
r=45

while True:
    tStart=time.time()
    im=picam2.capture_array()
    print(im[20,20])
    cv2.putText(im,str(int(fps))+' FPS',pos,font,height,myColor,weight)
    cv2.rectangle(im, upperLeft,lowerRight,rColor, thickness)
    cv2.circle(im, cent, r, rColor, thickness)
    cv2.imshow("picam2",im)
    if cv2.waitKey(1)==ord('q'):
        break
    tEnd=time.time()
    loopTime=tEnd-tStart
    fps=.9*fps +.1*(1/loopTime)
    #print(int(fps))
cv2.destroyAllWindows()