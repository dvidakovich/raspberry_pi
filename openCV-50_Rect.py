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

rColor=(255,0,255)
thickness=7

cent=(145,245)
r=45

while True:
    tStart=time.time()
    frame=picam2.capture_array()
    # Draw rectangles in the frame
    frame[:int(dispW/2),int(dispH/2):] = (0,0,255)
    frame[:int(dispW/2),:int(dispH/2)] = (255,0,0)
    frame[int(dispW/2):,:int(dispH/2)] = (0,255,0)
    cv2.putText(frame,str(int(fps))+' FPS',pos,font,height,myColor,weight)
    cv2.imshow("picam2",frame)
    if cv2.waitKey(1)==ord('q'):
        break
    tEnd=time.time()
    loopTime=tEnd-tStart
    fps=.9*fps +.1*(1/loopTime)
    #print(int(fps))
cv2.destroyAllWindows()