#include <iostream>
#include <fstream>
#include <string>
#include <algorithm> // std::sort
#include <opencv2/opencv.hpp>

using namespace cv;
using namespace std;

/// Global Variables
char *filename;
Mat image;
const int Number_of_questions = 20;

int DELAY_BLUR = 10;
int MAX_KERNEL_LENGTH = 4;
char window_name[] = "Filter Demo 1";

vector<KeyPoint> FindingBlobs(Mat &image, int minArea, int maxArea){

  // -------- FINDING BLOBS ----------

	// Setup SimpleBlobDetector parameters.
	SimpleBlobDetector::Params params;

	// Change thresholds
	params.minThreshold = 10;
	params.maxThreshold = 200;

	// Filter by Area.
	params.filterByArea = true;
	params.minArea = minArea;
    params.maxArea = maxArea;

	// Filter by Circularity
	params.filterByCircularity = true;
	params.minCircularity = 0.6;
    params.maxCircularity = 0.9;

	// Filter by Convexity
	params.filterByConvexity = true;
	params.minConvexity = 0.5;
    //params.maxConvexity =  0.5;

	// Filter by Inertiaå
	params.filterByInertia = true;
	params.minInertiaRatio = 0.01;

	// Storage for blobs
	vector<KeyPoint> keypoints;


	#if CV_MAJOR_VERSION < 3   // If you are using OpenCV 2

		// Set up detector with params
		SimpleBlobDetector detector(params);

		// Detect blobs
		detector.detect( im, keypoints);
	#else 

		// Set up detector with params
		Ptr<SimpleBlobDetector> detector = SimpleBlobDetector::create(params);   

		// Detect blobs
		detector->detect( image, keypoints);
	#endif 

	// Draw detected blobs as red circles.
	// DrawMatchesFlags::DRAW_RICH_KEYPOINTS flag ensures
	// the size of the circle corresponds to the size of blob

    return keypoints;
}

bool point_x_comparator(const KeyPoint& p1, const KeyPoint& p2) {
    return (p1.pt.x < p2.pt.x);
}
bool point_y_comparator(const KeyPoint& p1, const KeyPoint& p2) {
    return (p1.pt.y < p2.pt.y);
}
bool point_comparator(const KeyPoint& p1, const KeyPoint& p2) {
    return (p1.pt.x*1000+p1.pt.y < p2.pt.x*1000+p2.pt.y );
}

float autocorrect(string answerkeyfile, string answerfile, int percentage){
	
	// ----  open image ----- //
	string line_Ans, line_Cheat;
	int score = 0;
	Point2d line_Ans_d, line_Cheat_d;
	
	double x_gab, y_gab, x_ans, y_ans;
	char brackets1, comma, brackets2;

	ifstream answers (answerfile); // Answers
	ifstream answerkey (answerkeyfile); // CheatSheet
    
	while (answers >> brackets1 >> x_ans >> comma >> y_ans >> brackets2 && 
			answerkey >> brackets1 >> x_gab >> comma >> y_gab >> brackets2)
	{
    	//cout << x_ans << " " << y_ans << endl;
		if (x_ans+y_ans <= x_gab+y_gab*(1+percentage/100) || x_ans+y_ans >= x_gab+y_gab*(1-percentage/100)){
			// printf("x_ans + y_ans = %lf\n",x_ans+y_ans);
			// printf("x_gab + y_gab * 1.05  = %lf\n",x_gab+y_gab*1.05 );
			// printf("x_gab + y_gab * 0.95 = %lf\n",x_gab+y_gab*0.95);
	 		score++;
	 	}
	}
	cout << "Final Score is: " << score << '\n';
    answers.close();
	answerkey.close();
	
	return score;
}
 
double angle(const Point& v1, const Point& v2){
    double cosAngle = v1.dot(v2) / (norm(v1) * norm(v2));
	printf("CosAngle = %lf\n", cosAngle);
    if (cosAngle > 1.0)
        return 0.0;
    else if (cosAngle < -1.0)
        return CV_PI;
    return acos(cosAngle);
}

Mat rotate(Mat src, double angle){
    Mat dst;
    Point2f pt(src.cols/2., src.rows/2.);    
    Mat r = getRotationMatrix2D(pt, angle, 1.0);
    warpAffine(src, dst, r, Size(src.cols, src.rows));
    return dst;
}

// int display_dst( int delay )
// {
// 	imshow( window_name, image );
// 	int c = waitKey ( delay );
// 	if( c >= 0 ) { return -1; }
// 	return 0;
// }

int main(int argvc , char** argv){
    
    // ----  open image ----- //

        if (argvc != 2) {
            cerr << "Usage: " << argv[0] << " <img_path>" << endl;
            return 1;
        }

    filename = argv[1];
    image = imread(filename,IMREAD_GRAYSCALE);
	threshold(image, image, 200, 255, CV_THRESH_BINARY);

    // ----  Resize image ----- //1654 × 2339
	//1240 × 1753

	Size size(1240/2,1753/2);
    resize(image,image,size);//resize image

	/* Gauss filter
	for ( int i = 1; i < MAX_KERNEL_LENGTH; i = i + 2 )
    { GaussianBlur( image, image, Size( i, i ), 0, 0 );
      if( display_dst( DELAY_BLUR ) != 0 ) { return 0; } }
	*/

    // ----- Finding big Blobs ------ //
    vector<KeyPoint> keypoints = FindingBlobs(image,400,1000);

	stable_sort(keypoints.begin(), keypoints.end(), point_comparator); // sorting answers

	Mat im_with_keypoints;
	drawKeypoints( image, keypoints, im_with_keypoints, Scalar(0,0,255), DrawMatchesFlags::DRAW_RICH_KEYPOINTS );
    rectangle(im_with_keypoints, keypoints[0].pt,keypoints[3].pt, 127, 1, 8, 0);

    // Show blobs
    imwrite("img/Ans1_findblobs.jpg", im_with_keypoints);
	imshow("keypoints", im_with_keypoints );
	waitKey(0);

	for(int i=0; i < keypoints.size(); i++){
		printf("[%d,%d] \n", (int)keypoints[i].pt.x, (int)keypoints[i].pt.y);
	}
		printf("\n");

    // ----- Rotation ------ //
	double correct_angle = angle(keypoints[0].pt,keypoints[1].pt);
	printf("ANGLE: %lf\n",correct_angle);
	image = rotate(image,correct_angle);

	imwrite("correct_rotation.jpg", image);
	imshow("rotation", image);
    waitKey(0);

	// ----- Region of interest ------ //
    Rect roi(keypoints[1].pt,keypoints[4].pt);
    Mat ROI(image, roi);
	
	Size size2(174,607);
    resize(ROI,ROI,size2);//resize image

    // ----- Finding small Blobs ------ //

    keypoints = FindingBlobs(ROI, 100, 500);
	drawKeypoints( ROI, keypoints, im_with_keypoints, Scalar(0,0,255), DrawMatchesFlags::DRAW_RICH_KEYPOINTS );
    
    // Show blobs
    imwrite("img/Ans1_findAnswers.jpg", im_with_keypoints);
	imshow("Answers", im_with_keypoints );
	waitKey(0);

    // ------ Saving answers ------ //
	stable_sort(keypoints.begin(), keypoints.end(), point_y_comparator); // sorting answers
	
	ofstream myfile;
  	myfile.open ("Answer_1.txt");
	for(int i=0; i < keypoints.size(); i++){
		myfile << keypoints[i].pt;
	}
  	myfile.close();
	
	float Score = autocorrect("gabarito.txt", "Answer_1.txt", 5);



  return 0;
}   

