#include "opencv2/objdetect.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/imgproc.hpp"
#include "opencv2/videoio.hpp"
#include <opencv4/opencv2/core.hpp>

#include <bits/types/time_t.h>
#include <iostream>
#include <string>
#include <time.h>

void detectAndDisplay(cv::Mat frame);
void detectAndReturnEyes(cv::Mat input, cv::Mat* olho);
cv::CascadeClassifier face_cascade;
cv::CascadeClassifier eyes_cascade;
std::vector<cv::Rect> eyes;

int main(int argc, const char** argv)
{
  std::string face_cascade_name = "/home/andre/gits/opencv/data/haarcascades/haarcascade_frontalface_alt.xml";
  std::string eyes_cascade_name = "/home/andre/gits/opencv/data/haarcascades/haarcascade_eye_tree_eyeglasses.xml";
  
  // Carregando os cascades
  if (!face_cascade.load(face_cascade_name))
  {
    std::cout << "Erro carregando face cascade\n";
    return -1;
  };
  if (!eyes_cascade.load(eyes_cascade_name))
  {
    std::cout << "Erro carregando eyes cascade\n";
    return -1;
  };

  // Capturando da webcam
  int camera_device = 0;
  cv::VideoCapture capture;
  capture.open(camera_device);
  if (! capture.isOpened())
  {
    std::cout << "Erro ao capturar video\n";
    return -1;
  }

  // calculando FPS
  time_t start, end;
  int num_frames = 0;
  cv::Mat frame;

  // sequencia de nome dos arquivos de saida
  int seq_arq = 0;

  // loop principal
  while (capture.read(frame))
  {
    num_frames++;
    time(&start);

    if(frame.empty())
    {
      std::cout << "Erro ao capturar frame -- Break!\n";
      break;
    }
    // Aplica o classificador ao frame corrente
    //detectAndDisplay(frame);

    cv::Mat olhos[2];
    cv::Mat bw_olhos[2];
    detectAndReturnEyes(frame, olhos);

    // aplica filtro nas matrizes dos olhos
    if (eyes.size() > 0)
    {
      olhos[0].copyTo(bw_olhos[0]);
      olhos[1].copyTo(bw_olhos[1]);

      // calcula a media de intensidade
      cv::Scalar avg = cv::mean(bw_olhos[0]);

      // imprime a media (DEBUG)
      //std::cout << *avg.val << std::endl;

      // aplica o threshold
      cv::threshold(olhos[0], bw_olhos[0], *avg.val, 255, cv::ADAPTIVE_THRESH_GAUSSIAN_C);
      seq_arq++;
      
      // mostra imagem final
      cv::imshow("1", bw_olhos[0]);

      // salva imagens para treinamento de direção
      std::string output_file = std::to_string(seq_arq);
      std::cout << "olho_" << output_file << ".png" << std::endl;
      cv::imwrite("olho_"+output_file+".png", bw_olhos[0]);
    }

    // Sai caso tecla ESC seja pressionada
    if(cv::waitKey(1) == 27) break;

     // mostra FPS
    time(&end);
    double sec = difftime(end, start);
    if (sec >= 1.0f)
    {
      std::cout << "FPS: "    << num_frames;
      std::cout << "\t# olhos: " << eyes.size() << std::endl;
      num_frames = 0;
    }
  }
  return 0;
}

void detectAndDisplay(cv::Mat frame)
{
  cv::Mat frame_gray;
  cv::Mat faceROI;
  cv::Mat olho[2];

  cv::cvtColor(frame, frame_gray, cv::COLOR_BGR2GRAY);
  cv::equalizeHist(frame_gray, frame_gray);

  std::vector<cv::Rect> faces;

  // detecta faces
  face_cascade.detectMultiScale(frame_gray, faces);
  
  // executa detecção do olho somente se pelo menos 1 face for detectada
  if (faces.size() > 0)
  {
    // detecta olhos somente de uma face (a primeira da lista)
    faceROI = frame_gray(faces[0]);
    eyes_cascade.detectMultiScale(faceROI, eyes);
    if (eyes.size() > 0)
    {
      // isola olho (somente o primeiro da lista)
      olho[0] = faceROI(eyes[0]);
      cv::rectangle(faceROI, eyes[0], cv::Scalar(255, 255, 0));
      if (eyes.size() == 2)
      {
        olho[1] = faceROI(eyes[1]);
        cv::rectangle(faceROI, eyes[1], cv::Scalar(255, 255, 0));
      }
    }
  }

  // mostra face e olho(s)
  if (faces.size() > 0) cv::imshow("Face", faceROI);
  if (eyes.size() > 0)
  {
    cv::imshow("Olho 1", olho[0]);
    if (eyes.size() == 2) cv::imshow("Olho 2", olho[1]);
  }
}

// cv::Mat olho deve ter tamanho 2
void detectAndReturnEyes(cv::Mat input, cv::Mat* olho)
{
  cv::Mat frame_gray;
  cv::Mat faceROI;

  cv::cvtColor(input, frame_gray, cv::COLOR_BGR2GRAY);
  cv::equalizeHist(frame_gray, frame_gray);
  std::vector<cv::Rect> faces;

  face_cascade.detectMultiScale(frame_gray, faces);
  if (faces.size() > 0)
  {
    faceROI = frame_gray(faces[0]);
    eyes_cascade.detectMultiScale(faceROI, eyes);
    if (eyes.size() > 0)
    {
      olho[0] = faceROI(eyes[0]);
      if (eyes.size() == 2) olho[1] = faceROI(eyes[1]);
    }
  }

}
