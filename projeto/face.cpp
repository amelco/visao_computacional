#include "opencv2/objdetect.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/imgproc.hpp"
#include "opencv2/videoio.hpp"
#include <bits/types/time_t.h>
#include <iostream>
#include <string>
#include <time.h>

void detectAndDisplay( cv::Mat frame );
cv::CascadeClassifier face_cascade;
cv::CascadeClassifier eyes_cascade;

std::string face_file, eye_file;

int main( int argc, const char** argv )
{
  std::string face_cascade_name = "/home/andre/gits/opencv/data/haarcascades/haarcascade_frontalface_alt.xml";
  std::string eyes_cascade_name = "/home/andre/gits/opencv/data/haarcascades/haarcascade_eye_tree_eyeglasses.xml";
  
  //-- 1. Load the cascades
  if( !face_cascade.load( face_cascade_name ) )
  {
    std::cout << "--(!)Error loading face cascade\n";
    return -1;
  };
  if( !eyes_cascade.load( eyes_cascade_name ) )
  {
    std::cout << "--(!)Error loading eyes cascade\n";
    return -1;
  };
  int camera_device = 0;
  cv::VideoCapture capture;
  //-- 2. Read the video stream
  capture.open( camera_device );
  if ( ! capture.isOpened() )
  {
    std::cout << "--(!)Error opening video capture\n";
    return -1;
  }

  time_t start, end;
  int num_frames = 0;
  cv::Mat frame;
  while ( capture.read(frame) )
  {
    double fps_vg = capture.get(cv::CAP_PROP_FPS);
    num_frames++;
    time(&start);
    if( frame.empty() )
    {
      std::cout << "--(!) No captured frame -- Break!\n";
      break;
    }
    //-- 3. Apply the classifier to the frame
    detectAndDisplay( frame );
    if( cv::waitKey(10) == 27 )
    {
      break; // escape
    }
    time(&end);
    double sec = difftime(end, start);
    if (sec >= 1.0f)
    {
      std::cout << "video.get FPS: " << fps_vg;
      std::cout << " \tc++ FPS: "    << num_frames << std::endl;
      num_frames = 0;
    }
  }
  return 0;
}

void detectAndDisplay( cv::Mat frame )
{
  cv::Mat frame_gray;
  cv::Mat rosto;
  cv::Mat olho;
  cv::cvtColor( frame, frame_gray, cv::COLOR_BGR2GRAY );
  cv::equalizeHist( frame_gray, frame_gray );
  //-- Detect faces
  std::vector<cv::Rect> faces;
  std::vector<cv::Rect> eyes;
  face_cascade.detectMultiScale( frame_gray, faces );
  if (faces.size() > 0)
  {
    rosto = frame(faces[0]);
    cv::rectangle(frame, faces[0], cv::Scalar( 255, 0, 255 ));
    cv::Mat faceROI = frame_gray( faces[0] );
    eyes_cascade.detectMultiScale( faceROI, eyes );
    if (eyes.size() > 0)
    {
      olho = faceROI(eyes[0]);
    }
  }
  std::cout << "# olhos: " << eyes.size() << std::endl;

  cv::imshow("Capture - Face detection", frame);
  //if (faces.size() > 0) cv::imshow("Capture - Rosto", rosto);
  if (eyes.size() > 0) cv::imshow("Capture - Olho", olho);
}
