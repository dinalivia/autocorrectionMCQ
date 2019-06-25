#!/usr/bin/python

# Standard imports
import cv2
import numpy as np
import argparse

# Non standard imports
import imageprocessing as improc


#instantiate the parser
parser = argparse.ArgumentParser(description=
                              "Get ROI image app, \
                              arg1 = image path, \
                              arg2 = roi img path")

parser.add_argument('img_path', type=str,
                  help='Enter the file path')
parser.add_argument('roi_path', type=str,
                  help="Enter destination for ROI img")
args = parser.parse_args()
  

# Read reference image
img = cv2.imread("../img/Gabarito-preenchido.jpg", cv2.IMREAD_GRAYSCALE)
print('Original Dimensions 1: ',img.shape)
width = int(img.shape[1]/3)
height = int(img.shape[0]/3)
dim = (width, height)

# Resize reference image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)  
print('Resized Dimensions 1: ',resized.shape)
#cv2.imshow("Resized image 1", resized)
#cv2.waitKey(0)


# Read new image
# im = cv2.imread("otsu.jpg", cv2.IMREAD_GRAYSCALE)
# im = cv2.imread("../../img/gabarito.jpg", cv2.IMREAD_GRAYSCALE)
im = cv2.imread(args.img_path, cv2.IMREAD_GRAYSCALE)

# Resize new image
im = cv2.resize(im, dim, interpolation = cv2.INTER_AREA) 
print('Resized Dimensions 2: ',im.shape) 
#cv2.imshow("Resized image 2", im)
#cv2.waitKey(0)

# Find big blobs 
keypoints = improc.findBlobs (im, 400, 800)
print(keypoints)

# Sort keypoints and filter area
keypoints = improc.filterBlobs(keypoints, dim, 0.2)
print("filterBlobs")
print(keypoints)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob
im_keypts = cv2.drawKeypoints(im, keypoints,
                              np.array([]), (0,0,255),
                              cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show blobs
#cv2.imshow("keypoints", im_keypts)
#cv2.waitKey(0)
cv2.imwrite("Keypoints.jpg", im_keypts)

# FIXME
# Draw Region of Interest (ROI)
cv2.rectangle(im, (int(keypoints[0].pt[0]), int(keypoints[0].pt[1])),(int(keypoints[2].pt[0]), int(keypoints[2].pt[1])),127, 2)

# Show ROI
#cv2.imshow("ROI", im)
#cv2.waitKey(0)

# Correct rotation
pt1 = [int(keypoints[0].pt[0]), int(keypoints[0].pt[1])]
pt2 = [int(keypoints[1].pt[0]), int(keypoints[1].pt[1])]
pt3 = [int(keypoints[3].pt[0]), int(keypoints[3].pt[1])]
pt4 = [int(keypoints[2].pt[0]), int(keypoints[2].pt[1])]
angle = improc.angle(pt1,pt2)
img = improc.rotate(im,angle,im.shape)

# Show Rotated image
#cv2.imshow("Rotated", img)
#cv2.waitKey(0)

# Extract ROI
# imcrop  = im[pt1[1]:pt4[1], pt2[0]:pt3[0]]
imcrop  = im[pt1[1]:pt3[1], pt3[0]:pt2[0]]

# Print keypoints
for keyPoint in keypoints:
    x = keyPoint.pt[0]
    y = keyPoint.pt[1]
    s = keyPoint.size
    print('[' + str(x) + ',' + str(y) + ']\n')

# Show Rotated ROI
cv2.imwrite(args.roi_path,imcrop)
#cv2.imshow("roi", imcrop)
#cv2.waitKey(0)

cv2.destroyAllWindows()
