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

# Non standard imports
import imageprocessing as improc

# Read Region of Interest
# img = cv2.imread("gabarito_roi.png", cv2.IMREAD_GRAYSCALE)
img = cv2.imread("../gabarito/gabarito_roi.png", cv2.IMREAD_GRAYSCALE)
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
cv2.imwrite("../imgs/Keypoints.jpg", im_keypts)

# create list with keys
key = col.deque([])
for i in range(0,len(pts)):
    x = int(pts[i].pt[0])
    y = int(pts[i].pt[1])
    key.append(str(y*height+x))

print(key)

# mapping answers and saving to csv file 
answers = csv.writer(open("../answers/answers.csv","wb"), delimiter=',')
print("len(pts)")
print(len(pts))

# writing csv header
answers.writerow(["Qnumber","alternative","x_pos","y_pos", "key"])
alternative = col.deque([])
question = 1

# compare answer key with labeled keys from labels.csv
with open('../labels/labels.csv', 'rb') as csvfile:
    labels = csv.reader(csvfile, delimiter=',')
    linecount = 0
    for row in labels:
        print(row[0])
        if(linecount==0):
            linecount+=1
        elif(len(key)>0):
            print(key[0])
            print(row[4])
            print("key deve estar entre")
            print(int(row[4])+int(row[4])*0.001)
            print("and")
            print(int(row[4])-int(row[4])*0.001)

            # check if answer key is within
            # any labeled key range
            if((int(key[0]) <= int(row[4])+12) and
               (int(key[0]) >= int(row[4])-12)):
                print("MAPEANDO...")
                # copy info from labeled row to answers.csv
                answers.writerow([row[0],
                                  row[1],
                                  row[2],
                                  row[3],
                                  row[4]])
                key.popleft()
            else:
                print("Answer not mapped")
            linecount+=1
        
