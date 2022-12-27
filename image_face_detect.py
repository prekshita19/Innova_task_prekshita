{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "07781b1c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-1"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#importing open cv library\n",
    "\n",
    "import cv2\n",
    "import numpy as np\n",
    "\n",
    "#dataset load \n",
    "trainedData=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')\n",
    "\n",
    "#choose a image\n",
    "\n",
    "img=cv2.imread('one.jpg')\n",
    "\n",
    "#Conversion to black and white (grayscale)\n",
    "\n",
    "#grayimg=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)\n",
    "#print(grayimg)\n",
    "\n",
    "#detect faces\n",
    "\n",
    "faceCoordinates = trainedData.detectMultiScale(img)\n",
    "#print(faceCoordinates)\n",
    "  \n",
    "for i in range(0,9): \n",
    "\n",
    "    x,y,w,h=faceCoordinates[i]\n",
    "    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)\n",
    "\n",
    "cv2.imshow('person', img) \n",
    "cv2.waitKey()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9f31e200",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e4628bb0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
