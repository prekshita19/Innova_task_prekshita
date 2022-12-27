#importing open cv library

import cv2
from IPython.display import Video

from random import randrange as r 
#dataset load

trainedData=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#start the webcam
cam = cv2.VideoCapture("video1.mp4")

while True:

    success,frame=cam.read()

#Conversion to black and white(grayscale) 
#graying=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

#detect faces
faceCoordinates=trainedData.detectMultiScale(graying)

for x,y,w,h in faceCoordinates: 
    cv2.rectangle(frame, (x,y), (x+w, y+h), (r(0,256),r(0,256),r(0,256)),2)

cv2.imshow('frame', frame)
key=cv2.waitKey(1) 
if (key==81 or key==113):
    break

cam.release()