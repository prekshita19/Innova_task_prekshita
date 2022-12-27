{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d36db863",
   "metadata": {},
   "outputs": [],
   "source": [
    "#importing open cv library\n",
    "\n",
    "import cv2\n",
    "from IPython.display import Video\n",
    "\n",
    "from random import randrange as r \n",
    "#dataset load\n",
    "\n",
    "trainedData=cv2.CascadeClassifier(\"haarcascade_frontalface_default.xml\")\n",
    "\n",
    "#start the webcam\n",
    "cam = cv2.VideoCapture(\"video1.mp4\")\n",
    "\n",
    "while True:\n",
    "\n",
    "    success,frame=cam.read()\n",
    "\n",
    "#Conversion to black and white(grayscale) \n",
    "#graying=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)\n",
    "\n",
    "#detect faces\n",
    "faceCoordinates=trainedData.detectMultiScale(graying)\n",
    "\n",
    "for x,y,w,h in faceCoordinates: \n",
    "    cv2.rectangle(frame, (x,y), (x+w, y+h), (r(0,256),r(0,256),r(0,256)),2)\n",
    "\n",
    "cv2.imshow('frame', frame)\n",
    "key=cv2.waitKey(1) \n",
    "if (key==81 or key==113):\n",
    "    break\n",
    "\n",
    "cam.release()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "84e41135",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "990df7ac",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "651e74f7",
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
