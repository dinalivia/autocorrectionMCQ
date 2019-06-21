# -------------------------------------
# Answersheet autocorrection
# --
#
# Developed by Dina Livia - 10.06.2019
# --------------------------------------

#!/usr/bin/python

# Standard imports
import cv2
import numpy as np;

# Non standard imports
import imageprocessing as improc


# Read Region of Interest
img = cv2.imread("rotated.png", cv2.IMREAD_GRAYSCALE)
print('Original Dimensions 1: ',img.shape)
width = int(img.shape[1])
height = int(img.shape[0])
dim = (width, height)

# Find small blobs
pts = improc.findBlobs(img, 100, 200)

# Ordenate blobs (filter)
pts = improc.filterBlobs(pts, dim, 0.02)

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

# Draw answers limits
improc.drawlimits(img, dim, 5, 20, 0.1, 0.028)

# Convert keypoints as alphabetic answers
#improc.labelanswers(im_keypts)
 
