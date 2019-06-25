# -------------------------------------
# Image Processing Methods
# --
#
# Developed by Dina Livia - 10.06.2019
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
    params.minArea = minArea #400 #100
    params.maxArea = maxArea #800 #200

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

def filterBlobs(pts, im_size, percentage):

    im_width = im_size[0]
    im_height = im_size[1]
    
    # Sort points
    #pts = sorted(pts, key=lambda pts:
                 #pts.pt[1]*im_height+pts.pt[0])

    # FIXME
    pts.sort(key=lambda points:
             int(int(points.pt[1])*im_height)+
             int(points.pt[0]))

    # Filter points from a certain margin
    pts = [points for points in pts
           if ((points.pt[1]>percentage*im_height)
               and (points.pt[1]>percentage*im_width))]

    # Print keypoints
    print("Sorting keypoints")
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

def drawlimits(img, imsize, numchoices, numquestions, marginH, marginV):
    # x = [margin,imsize[0]-margin]
    x0 = int(marginH*imsize[0])
    x1 = x0
    # y = [margin*imsize[1],imsize[1]-margin]
    y = int(marginV*imsize[1])
    
    for i in range(1,numquestions):
        for j in range(1, numchoices):
            x1 = x1 + int(imsize[0]/numchoices)
            #y = margin + imsize[1]/(numlines)
            cv2.line(img,(x0,y),(x1,y), (127,0,0),2)  
        y = y + int(imsize[1]/numquestions)
        cv2.imshow("limits", img)
        cv2.waitKey(0)

def labelanswers(keypts):
    #answer.txt
    return 0
