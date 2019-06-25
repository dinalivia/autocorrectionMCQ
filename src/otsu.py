''' 
	OpenCV Threshold Example
  Copyright 2015 by Satya Mallick <spmallick@gmail.com>
'''
# import opencv 
import cv2
import argparse

#instantiate the parser
parser = argparse.ArgumentParser(description=
                                 "Align image app, \
                                 arg1 = image path, \
                                 arg2 = binary img path")

parser.add_argument('img_path', type=str,
                    help='Enter the file path')
parser.add_argument('binary_path', type=str,
                    help="Enter destination for aligned img")
args = parser.parse_args()
  

# Read image 
src = cv2.imread(args.img_path, cv2.IMREAD_GRAYSCALE); 

#Otsu threhold
th, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU); 
cv2.imwrite(args.binary_path, dst); 
