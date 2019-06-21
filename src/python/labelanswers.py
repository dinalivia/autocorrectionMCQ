# -------------------------------------
# Label answers
# --
#
# Developed by Dina Livia - 10.06.2019
# --------------------------------------

#!/usr/bin/python

# Standard imports
import cv2
import numpy as np;
import csv
import collections as col

# Non standard imports
import imageprocessing as improc

# Read Region of Interest
# img = cv2.imread("gabarito_roi.png", cv2.IMREAD_GRAYSCALE)
img = cv2.imread("preenchido.png", cv2.IMREAD_GRAYSCALE)
print('Original Dimensions 1: ',img.shape)
width = int(img.shape[1])
height = int(img.shape[0])
dim = (width, height)

# Find small blobs
pts = improc.findBlobs(img, 100, 200)
print("len(pts)")
print(len(pts))

# Ordenate blobs (filter)
pts = improc.filterBlobs(pts, dim, 0.0)
print("len(pts)")
print(len(pts))

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob
im_keypts = cv2.drawKeypoints(img, pts,
                              np.array([]), (0,0,255),
                              cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show blobs
cv2.imshow("keypoints", im_keypts)
cv2.waitKey(0)
cv2.imwrite("Keypoints.jpg", im_keypts)

# saving answers to csv file 
labels = csv.writer(open("labels.csv","wb"), delimiter=',')
print("len(pts)")
print(len(pts))

# csv header
labels.writerow(["Qnumber","alternative","x_pos","y_pos","key"])

# alternatives and starting point for questions
alternative = col.deque(['a','b','c','d','e'])
question = 1

# write csv file
for i in range(0,len(pts)):
    #for j in range(0, 5):
    x = int(pts[i].pt[0])
    y = int(pts[i].pt[1])
    labels.writerow([question,
                     alternative[0],
                     str(x),
                     str(y),
                     str(y*height+x)])
    alternative.rotate(-1)
    if(alternative[0]=='a'):
        question = question + 1
