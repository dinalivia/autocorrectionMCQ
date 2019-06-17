#!/usr/bin/python

# Standard imports
import cv2
import numpy as np;

# Read image
img = cv2.imread("../../img/doc-2.jpg", cv2.IMREAD_GRAYSCALE)
print('Original Dimensions 1: ',img.shape)
width = int(img.shape[1]/3)
height = int(img.shape[0]/3)
dim = (width, height)

resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
  
print('Resized Dimensions : ',resized.shape)
 
cv2.imshow("Resized image 1", resized)
cv2.waitKey(0)

# Read image
im = cv2.imread("otsu.jpg", cv2.IMREAD_GRAYSCALE)

im = cv2.resize(im, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',im.shape)
 
cv2.imshow("Resized image 2", im)
cv2.waitKey(0)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 10
params.maxThreshold = 200


# Filter by Area.
params.filterByArea = True
params.minArea = 400
params.maxArea = 800

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.1

# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.87
    
# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.01

# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
	detector = cv2.SimpleBlobDetector(params)
else : 
	detector = cv2.SimpleBlobDetector_create(params)


# Detect blobs.
keypoints = detector.detect(im)
for keyPoint in keypoints:
    x = keyPoint.pt[0]
    y = keyPoint.pt[1]
    s = keyPoint.size
    print('[' + str(x) + ',' + str(y) + ']\n') 

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob

im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show blobs
cv2.imshow("keypoints",im_with_keypoints)
cv2.waitKey(0)
cv2.imwrite("Keypoints.jpg", im_with_keypoints)
#cv2.waitKey(0)
cv2.destroyAllWindows()
