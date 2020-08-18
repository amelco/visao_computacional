# Prova

**Aluno:** Andre Herman Freire Bezerra  
**Matrícula:** 20202000080

1. Qual é a diferença entre processamento digital de imagens, computação gráfica
e visão computacional?

**Processamento digital**: Qualquer tipo de tratamento feito digitalmente (através de computadores)
em uma imagem digital ou digitalizada. Os tratamentos incluem, mas não são limitados a:
- redimensionamento
- aplicação de filtros

**Computação gráfica**: Criação de imagens ou vídeos utilizando apenas o computador.

**Visão computacional**: A criação de sistemas artificiais que obtém informação de imagens como um meio
a se fazer com que uma máquina "enxergue".

2. Qual é a função de uma equalização de histograma?

É um método de ajuste de constraste no processamento de imagens que utiliza seu histograma. 
É um método que busca o aprimoramento da imagem, acentuando detalhes não visíveis anteriormente, provendo uma melhor qualidade sem perder informação. 

3. Como você explicaria a operação de convolução bidimensional?

É um operador matemático linear que, a partir de duas funções, resulta numa terceira que expressa como uma é modificada pela outra.
É definida pela integral do produto de duas funções depois que uma é invertida e deslocada sobre a outra.
Em imagens, a convolução é feita numericamente, já que as funções não são contínuas, e sim, discretas.

5. O que são features?

São quaisquer características que podem ser identificadas em uma imagem. Exemplos: linhas, formas geométricas e objetos.

6. Qual é a diferença entre matriz intrínseca e extrínseca?

A matriz intrínseca contém os parâmetros de uma câmera com informações associadas às características inerentes à ela.
A representação de uma matriz intrínseca é criada levando em  conta  centro  ótico da  câmera e  o  plano da imagem  gerada  por ela.

A  matriz  dos  parâmetros  extrínsecos é uma  matriz que contém a posição e orientação da câmera. 
A orientação da câmera é representada por uma matriz e é chamada de matriz de rotação. 
A posição da câmera é representada por outra matriz, chamada de matriz  de  translação.
Essa  matriz é  a  distância  do  centro  da  câmera  até  o  sistema  de coordenadas  adotado  como  principal. 

7. Como funcionam as redes convolucionais?

É uma classe das redes neurais, frequentemente utilizadas em análises de imagens.
São inspiradas por processos biológicos em que o padrão de conectividade entre os neurônios se assemelha à organização do córtex visual de animais.
Neurônios individuais respondem a estímulos de uma região do campo visual conhecido como campo receptor.
Os campos receptores de diferentes neuronios se sobrepõem parcialmente de forma a cobrir todo o campo visual.

Uma rede neural convolucional consiste em uma camada de entrada e uma de saída, bem como em várias camadas ocultas. 
As camadas ocultas normalmente consistem de uma série de camadas convolucionais que convoluem com uma multiplicação ou produto escalar. 
A função de ativação é comumente uma camada RELU e é subsequentemente seguida por convoluções adicionais, 
como camadas agrupadas (pooling layers), camadas totalmente conectadas e camadas de normalização.
São chamadas de camadas ocultas porque suas entradas e saídas são mascaradas pela função de ativação e convolução final.

Embora as camadas sejam coloquialmente chamadas de convoluções, isso ocorre apenas por convenção. 
Matematicamente, é tecnicamente um produto escalar móvel ou correlação cruzada. 
Isso é significativo para os índices na matriz, pois afeta como o peso é determinado em um ponto de índice específico.
