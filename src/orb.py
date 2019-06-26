from __future__ import print_function
import cv2
import numpy as np
import argparse


MAX_MATCHES = 500
GOOD_MATCH_PERCENT = 0.5


def alignImages(im1, im2):

  # Convert images to grayscale
  im1Gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
  im2Gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
  
  # Detect ORB features and compute descriptors.
  #orb = cv2.ORB_create(MAX_MATCHES)
  orb = cv2.ORB(MAX_MATCHES)
  keypoints1, descriptors1 = orb.detectAndCompute(im1Gray, None)
  keypoints2, descriptors2 = orb.detectAndCompute(im2Gray, None)
  
  # Match features.
  #matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
  matcher = cv2.DescriptorMatcher_create("BruteForce-Hamming")
  matches = matcher.match(descriptors1, descriptors2, None)
  
  # Sort matches by score
  matches.sort(key=lambda x: x.distance, reverse=False)

  # Remove not so good matches
  numGoodMatches = int(len(matches) * GOOD_MATCH_PERCENT)
  matches = matches[:numGoodMatches]

  # Draw top matches
  #imMatches = cv2.drawMatches(im1, keypoints1, im2, keypoints2, matches, None)
  #cv2.imwrite("matches.jpg", imMatches)
  
  # Extract location of good matches
  points1 = np.zeros((len(matches), 2), dtype=np.float32)
  points2 = np.zeros((len(matches), 2), dtype=np.float32)

  for i, match in enumerate(matches):
    points1[i, :] = keypoints1[match.queryIdx].pt
    points2[i, :] = keypoints2[match.trainIdx].pt
  
  # Find homography
  h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)

  # Use homography
  height, width, channels = im2.shape
  im1Reg = cv2.warpPerspective(im1, h, (width, height))
  
  return im1Reg, h


if __name__ == '__main__':

  #instantiate the parser
  parser = argparse.ArgumentParser(description=
                                  "Align image app, \
                                  arg1 = image path, \
                                  arg2 = aligned img path")

  parser.add_argument('img_path', type=str,
                      help='Enter the file path')
  parser.add_argument('aligned_path', type=str,
                      help="Enter destination for aligned img")
  args = parser.parse_args()
  
  # Read reference image
  refFilename = "../img/doc-2.jpg"
  print("Reading reference image : ", refFilename)
  imReference = cv2.imread(refFilename, cv2.IMREAD_COLOR)
  
  # Read image to be aligned
  imFilename = args.img_path
  print("Reading image to align : ", imFilename);  
  im = cv2.imread(imFilename, cv2.IMREAD_COLOR)
  
  print("Aligning images ...")
  # Registered image will be resotred in imReg. 
  # The estimated homography will be stored in h. 
  imReg, h = alignImages(im, imReference)
  
  # Write aligned image to disk. 
  outFilename = args.aligned_path
  print("Saving aligned image : ", outFilename); 
  cv2.imwrite(outFilename, imReg)
  #cv2.imshow("alinhada", imReg)
  #cv2.waitKey(0)

  # Print estimated homography
  print("Estimated homography : \n",  h)

  # Read image 
  src = cv2.imread(outFilename, cv2.IMREAD_GRAYSCALE); 

  #Otsu threhold
  th, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU);
  print("Saving filtered image : ", outFilename); 
  cv2.imwrite("otsu.png", dst);
  #cv2.imshow("binaria", dst)
  #cv2.waitKey(0)
