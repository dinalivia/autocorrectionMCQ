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
  
print('Resized Dimensions 1: ',resized.shape)
 
cv2.imshow("Resized image 1", resized)
cv2.waitKey(0)

def findBlobs(img, minArea, maxArea):
        
        # Setup SimpleBlobDetector parameters.
        params = cv2.SimpleBlobDetector_Params()

        # Change thresholds
        params.minThreshold = 10
        params.maxThreshold = 200


        # Filter by Area.
        params.filterByArea = True
        params.minArea = minArea #400
        params.maxArea = maxArea #800

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
        keypoints = detector.detect(img)
        for keyPoint in keypoints:
                x = keyPoint.pt[0]
                y = keyPoint.pt[1]
                s = keyPoint.size
                print('[' + str(x) + ',' + str(y) + ']\n')

        return keypoints

def getsecond(pt):
        return (pt.pt[1])

def getfirst(pt):
        return (pt.pt[0])
        
def filterBlobs(pts, im_size, percentage):
        #FIXME
        pts = sorted(pts, key=getsecond)
        pts = sorted(pts, key=getfirst)

        pts = [points for points in pts if (points.pt[1]>0.2*height)]
        for keyPoint in pts:
                x = keyPoint.pt[0]
                y = keyPoint.pt[1]
                s = keyPoint.size
                print('[' + str(x) + ',' + str(y) + ']\n')
        return pts

# Read image
im = cv2.imread("otsu.jpg", cv2.IMREAD_GRAYSCALE)

im = cv2.resize(im, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions 2: ',im.shape)
 
cv2.imshow("Resized image 2", im)
cv2.waitKey(0)

keypoints = findBlobs (im, 400, 800)
print(keypoints)

keypoints = filterBlobs(keypoints, im.shape, 100)
print("filterBlobs")
print(keypoints)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob

im_with_keypoints = cv2.drawKeypoints(im, keypoints,
                                      np.array([]), (0,0,255),
                                      cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show blobs
cv2.imshow("keypoints",im_with_keypoints)
cv2.waitKey(0)
cv2.imwrite("Keypoints.jpg", im_with_keypoints)
#cv2.waitKey(0)
cv2.destroyAllWindows()

#FIXME
cv2.rectangle(im, (int(round(keypoints[0].pt[0])), int(round(keypoints[0].pt[1]))),(int(round(keypoints[3].pt[0])), int(round(keypoints[3].pt[1]))),(255,0,0), 2)

#cv2.rectangle(im, (int(round(keypoints[0]))),(int(round(keypoints[3]))),(255,0,0), 2)

cv2.imwrite("roi.png",im)

cv2.imshow("ROI", im)
cv2.waitKey(0)
