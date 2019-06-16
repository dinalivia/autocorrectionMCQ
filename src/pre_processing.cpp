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
int height, width;

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

float autocorrect(string filename){
	
	// ----  open image ----- //
	string line_Ans, line_Cheat;
	int score = 0;
	Point2d line_Ans_d, line_Cheat_d;
	
	double x_gab, y_gab, x_ans, y_ans;
	char brackets1, comma, brackets2;

	ifstream answers (filename); // Answers
	ifstream cheatsheet ("gabarito.txt"); // CheatSheet
    
	while (answers >> brackets1 >> x_ans >> comma >> y_ans >> brackets2 && 
			cheatsheet >> brackets1 >> x_gab >> comma >> y_gab >> brackets2)
	{
    	//cout << x_ans << " " << y_ans << endl;
		if (x_ans+y_ans <= x_gab+y_gab*1.05 || x_ans+y_ans >= x_gab+y_gab*0.95){
			// printf("x_ans + y_ans = %lf\n",x_ans+y_ans);
			// printf("x_gab + y_gab * 1.05  = %lf\n",x_gab+y_gab*1.05 );
			// printf("x_gab + y_gab * 0.95 = %lf\n",x_gab+y_gab*0.95);
	 		score++;
	 	}
	}
	cout << "Final Score is: " << score << '\n';
    answers.close();
	cheatsheet.close();
	
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

int histogram(Mat src, int img_width, int img_height){
  cout << "chamando o histogram" << '\n';

  Mat image = src;
  int width = img_width, height = img_height;
  Mat histR;
  int nbins = 128;
  float range[] = {0, 256};
  const float *histrange = { range };
  bool uniform = true;
  bool acummulate = false;

  cout << "largura = " << width << endl;
  cout << "altura  = " << height << endl;

  int histw = nbins, histh = nbins/2;
  Mat histImgR(histh, histw, CV_8UC3, Scalar(0,0,0));

    calcHist(&image, 1, 0, Mat(), histR, 1,
             &nbins, &histrange,
             uniform, acummulate);

    normalize(histR, histR, 0, histImgR.rows, NORM_MINMAX, -1, Mat());

    histImgR.setTo(Scalar(0));

    for(int i=0; i<nbins; i++){
      line(histImgR,
           Point(i, histh),
           Point(i, histh-cvRound(histR.at<float>(i))),
           Scalar(0, 0, 255), 1, 8, 0);
    }
    //histImgR.copyTo(image(Rect( 0, 0, nbins, histh)));
    imshow("histogram", histImgR);
	waitKey(0);
  return 0;
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
	width = image.size().width;
	height = image.size().height;

    image = rotate(image, 180);

	int p = histogram(image, width, height);

	//adaptiveThreshold(image, image, 255, ADAPTIVE_THRESH_GAUSSIAN_C, THRESH_BINARY, 25, 5);
	
	threshold(image, image, 0, 255, CV_THRESH_OTSU);

    // ----  Resize image ----- //1654 × 2339
	//1240 × 1753

	//Size size(1240/2,1753/2);
	Size size(width/2, height/2);
    resize(image,image,size);//resize image

	imshow("image_binary", image );
    waitKey(0);

  return 0;
}   


