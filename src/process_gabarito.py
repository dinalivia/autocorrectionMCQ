# ---------------------------------------
# Process KeyAnswersheet
# --
# Read ROI image of the key answer sheet,
# process and save answers as a csv file
# --
#
# Developed by Dina Livia - 10.06.2019
# ---------------------------------------

#!/usr/bin/python

# Standard imports
import cv2 
import numpy as np;
import csv
import collections as col
import argparse

# Non standard imports
import imageprocessing as improc

#instantiate the parser
parser = argparse.ArgumentParser(description=
                              "extract answers app, \
                              arg1 = image roi path, \
                              arg2 = answers csv path")

parser.add_argument('roi_path', type=str,
                  help='Enter the file path')
parser.add_argument('answer_path', type=str,
                  help="Enter destination for ROI img")
args = parser.parse_args()

# Read Region of Interest
# img = cv2.imread("gabarito_roi.png", cv2.IMREAD_GRAYSCALE)
img = cv2.imread(args.roi_path, cv2.IMREAD_GRAYSCALE)
print('Original Dimensions 1: ',img.shape)
width = int(img.shape[1])
height = int(img.shape[0])
dim = (width, height)

# Find small blobs
pts = improc.findBlobs(img, 100, 200)
print("len(pts)")
print(len(pts))

# Ordenate blobs (filter)
pts = improc.filterBlobs(pts, dim, 0.02)
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
cv2.imwrite("../imgs/Keypoints.jpg", im_keypts)

# create list with keys
key = ([])
for i in range(0,len(pts)):
    x = int(pts[i].pt[0])
    y = int(pts[i].pt[1])
    key.append([x,y])

print(key)

# mapping answers and saving to csv file 
answers = csv.writer(open(args.answer_path,"wb"), delimiter=',')
print("len(pts)")
print(len(pts))

# writing csv header
answers.writerow(["Qnumber","alternative","x_pos","y_pos", "key"])
#alternative = col.deque([])
question = 1


# compare answer key with labeled keys from labels.csv
with open('../labels/labels.csv', 'rb') as csvfile:
    labels = csv.reader(csvfile, delimiter=',')
    found = False
    linecount=0

    for k in range(0,len(key)):
        print("\n key[k]:" + str(key[k]))

        for row in labels:
            print(row)

            if linecount == 0:
                linecount+=1
                continue

            # check if answer key is within
            # any labeled key range
            minX =  int(row[2])-12
            maxX =  int(row[2])+12
            minY =  int(row[3])-12
            maxY =  int(row[3])+12

            if ((key[k][0] <= maxX and key[k][0] >= minX) and
            (key[k][1] <= maxY and key[k][1] >= minY)):
               
                print("MAPEANDO...")
                # copy info from labeled row to answers.csv
                answers.writerow([row[0],
                                  row[1],
                                  row[2],
                                  row[3],
                                  row[4]])
                break
            else:
                print("Answer not mapped")
                #key.rotate()

