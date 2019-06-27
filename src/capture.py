# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
#from matplotlib import pyplot as plt

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# allow the camera to warmup
time.sleep(0.1)

image = frame.array
h0 = hist(image.ravel(),256,[0,256])
count = 0

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    
    image = frame.array
    h = hist(image.ravel(),256,[0,256])

    # show the frame
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF

    path = "../img/teste/test" + str(count) + ".png"
    
    if(h0 < h-h*0.2 or h0 > h+h*0.2):
        cv2.imwrite(path, image)
        h0 = h
        count+=1
        print("Salvando foto")
        cv2.waitKey(1000)

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
