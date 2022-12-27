#importing open cv library

import cv2
import numpy as np

#dataset load 
trainedData=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#choose a image

img=cv2.imread('one.jpg')

#Conversion to black and white (grayscale)

#grayimg=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#print(grayimg)

#detect faces

faceCoordinates = trainedData.detectMultiScale(img)
#print(faceCoordinates)
  
for i in range(0,9): 

    x,y,w,h=faceCoordinates[i]
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)

cv2.imshow('person', img) 
cv2.waitKey()