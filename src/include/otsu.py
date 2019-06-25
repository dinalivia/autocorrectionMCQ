''' 
	OpenCV Threshold Example
  Copyright 2015 by Satya Mallick <spmallick@gmail.com>
'''
# import opencv 
import cv2 

# Read image 
src = cv2.imread("aligned.jpg", cv2.IMREAD_GRAYSCALE); 

#Otsu threhold
th, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU); 
cv2.imwrite("otsu-threshold.jpg", dst); 
