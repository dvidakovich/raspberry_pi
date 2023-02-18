import cv2
from picamera2 import Picamera2
import time
picam2 = Picamera2()
dispW = 1280
dispH = 720
picam2.preview_configuration.main.size = (dispW, dispH)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.controls.FrameRate = 40
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()
fps = 0
pos = (30, 60)
font = cv2.FONT_HERSHEY_SIMPLEX
height = 1.5
myColor = (0, 0, 255)
weight = 3

boxW=250
boxH=125
tlC=50
tlR=75
lrC=tlC+boxW
lrR=tlR+boxH
deltaC=2
deltaR=2
thickness=-1
Rcolor=(0,125,255)


while True:
    tStart = time.time()
    im = picam2.capture_array()
    cv2.putText(im, str(int(fps))+' FPS', pos, font, height, myColor, weight)
    if tlC+deltaC<0 or lrC+deltaC>dispW-1:
        deltaC=deltaC*(-1)
    if tlR+deltaR<0 or lrR+deltaR>dispH-1:
        deltaR=deltaR*(-1)
    tlC=tlC+deltaC
    tlR=tlR+deltaR
    lrC=lrC+deltaC
    lrR=lrR+deltaR
    cv2.rectangle(im, (tlC, tlR),(lrC,lrR),Rcolor,thickness)
    cv2.imshow("Camera", im)
    if cv2.waitKey(1) == ord('q'):
        break
    tEnd = time.time()
    loopTime = tEnd-tStart
    fps = .9*fps + .1*(1/loopTime)
cv2.destroyAllWindows()
