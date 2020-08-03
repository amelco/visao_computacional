#include "App.h"

int App::run()
{
  get_app_state();
  return 0;
}

App::App()
{
  condicao = "cal";
  calibration = true;
  arq_modelo = "trained_model.xml";
  dt = 1.0f;
}

App::App(int argc, char* argv[])
{
  App();
  if (argc > 1)
  {
    condicao = std::string(argv[1]);
    if (condicao.compare("use") == 0)
    {
      if (argc < 3)
      {
        show_usage(argv[0]);
        exit(1);
      }
      arq_modelo = argv[2];
    }
    else if (condicao.compare("cal") == 0) calibration = true;
    else 
    {
      show_usage(argv[0]);
      exit(1);
    }
  }
}

void App::show_usage(std::string app_name)
{
  std::cout << "Uso:\n" << app_name << " [condição] [arq_modelo] [dt]" << std::endl;
  std::cout << "condição:   'cal' para calibrar ou 'use' para utilizar modelo calibrado 'arq_modelo'" << std::endl;
  std::cout << "            OBS: se condição for 'use' deve-se especificar o arq_model" << std::endl;
  std::cout << "dt      :   intervalo de tempo (em segundos) entre predições" << std::endl;
}

void App::get_app_state()
{
  using namespace std;
  cout << "Método de utilização:\t";
  if (condicao.compare("cal") == 0)
  {
    cout << "Calibração" << endl;
  }
  else
  {
    cout << "Predição\nArquivo do modelo:\t" << arq_modelo << endl;
  }
  cout << "Tempo de atualização:\t" << dt << endl;
}
