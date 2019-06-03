// Got it from: https://github.com/spmallick/learnopencv/tree/master/ImageAlignment-FeatureBased
// edited

#include <opencv2/opencv.hpp>
#include "opencv2/xfeatures2d.hpp"
#include "opencv2/features2d.hpp"
 
using namespace std;
using namespace cv;
using namespace cv::xfeatures2d;
 
const int MAX_FEATURES = 500;
const float GOOD_MATCH_PERCENT = 0.15f;
 
void alignImages(Mat &im1, Mat &im2, Mat &im1Reg, Mat &h)
{

  // Convert images to grayscale
  Mat im1Gray, im2Gray;
  cvtColor(im1, im1Gray, CV_BGR2GRAY);
  cvtColor(im2, im2Gray, CV_BGR2GRAY);
   
  // Variables to store keypoints and descriptors
  std::vector<KeyPoint> keypoints1, keypoints2;
  Mat descriptors1, descriptors2;
   
  // Detect ORB features and compute descriptors.
  Ptr<Feature2D> orb = ORB::create(MAX_FEATURES);
  orb->detectAndCompute(im1Gray, Mat(), keypoints1, descriptors1);
  orb->detectAndCompute(im2Gray, Mat(), keypoints2, descriptors2);
   
  // Match features.
  std::vector<DMatch> matches;
  Ptr<DescriptorMatcher> matcher = DescriptorMatcher::create("BruteForce-Hamming");
  matcher->match(descriptors1, descriptors2, matches, Mat());
   
  // Sort matches by score
  std::sort(matches.begin(), matches.end());
   
  // Remove not so good matches
  const int numGoodMatches = matches.size() * GOOD_MATCH_PERCENT;
  matches.erase(matches.begin()+numGoodMatches, matches.end());
   
  // Draw top matches
  Mat imMatches;
  drawMatches(im1, keypoints1, im2, keypoints2, matches, imMatches);
  imwrite("matches.jpg", imMatches);
   
  // Extract location of good matches
  std::vector<Point2f> points1, points2;
   
  for( size_t i = 0; i < matches.size(); i++ )
  {
    points1.push_back( keypoints1[ matches[i].queryIdx ].pt );
    points2.push_back( keypoints2[ matches[i].trainIdx ].pt );
  }
   
  // Find homography
  h = findHomography( points1, points2, RANSAC );
   
  // Use homography to warp image
  warpPerspective(im1, im1Reg, h, im2.size());
   
}

int main(int argc, char **argv)
{
  // Read reference image
  string refFilename("../img/doc.jpg"); 
  cout << "Reading reference image : " << refFilename << endl; 
  Mat imReference = imread(refFilename);
  
  int width = imReference.size().width;
  int height = imReference.size().height;
  Size size1(width/2, height/2);
  resize(imReference,imReference,size1);//resize image

  imshow("reference_image", imReference);
  waitKey(0);
 
  // Read image to be aligned
  string imFilename("../img/pi_cam/test2.jpg");
  cout << "Reading image to align : " << imFilename << endl; 
  Mat im = imread(imFilename);

  width = im.size().width;
  height = im.size().height;
  Size size2(width/2, height/2);
  resize(im,im,size2);//resize image

  imshow("image_to_align", im);
  waitKey(0);
   
  // Registered image will be resotred in imReg. 
  // The estimated homography will be stored in h. 
  Mat imReg, h;
   
  // Align images
  cout << "Aligning images ..." << endl; 
  alignImages(im, imReference, imReg, h);
 
  // Write aligned image to disk. 
  string outFilename("aligned.jpg");
  cout << "Saving aligned image : " << outFilename << endl; 
  imwrite(outFilename, imReg);
  imshow("aligned_image", imReg);
  waitKey(0);
 
  // Print estimated homography
  cout << "Estimated homography : \n" << h << endl; 
   
}