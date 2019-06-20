# -------------------------------------
# Image Processing Methods
# --
#
# Developed by Dina Livia - 10.06.2019,
# Code inspired by LearnOpenCV tutorials
# --------------------------------------

#!/usr/bin/python

# Standard imports
import cv2
import numpy as np;



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
        
def filterBlobs(pts, im_height, percentage):
        #FIXME
        pts = sorted(pts, key=getsecond)
        pts = sorted(pts, key=getfirst)

        pts = [points for points in pts
               if (points.pt[1]>percentage*im_height)]

        for keyPoint in pts:
                x = keyPoint.pt[0]
                y = keyPoint.pt[1]
                s = keyPoint.size
                print('[' + str(x) + ',' + str(y) + ']\n')

        return pts

def angle(pt1, pt2):
    cosAngle = np.dot(pt1,pt2)/(
        np.linalg.norm(pt1)*np.linalg.norm(pt2))
    if (cosAngle > 1.0):
        return 0.0
    elif (cosAngle < -1.0):
        return np.pi
    return np.arccos(cosAngle)

def rotate(src, angle, imsize):
    width = int(imsize[1])
    height = int(imsize[0])
    center = (width / 2, height / 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(src, M, (width, height))
    return rotated
