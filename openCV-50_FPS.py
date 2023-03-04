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
    # Create a frame for FPS
    cv2.putText(frame,str(int(fps))+' FPS',pos,font,height,myColor,weight)
    #Show the frame
    cv2.imshow("picam2",frame)
    # Create an if statement to break the loop
    if cv2.waitKey(1)==ord('q'):
        break
    # Calculate the FPS
    tEnd=time.time()
    loopTime=tEnd-tStart
    fps=.9*fps +.1*(1/loopTime)
cv2.destroyAllWindows()