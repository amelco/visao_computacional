**Compilando**:
```
make
```

**Executando**:
```
./eyes
```

## Funcionamento

O objetivo final desse programa é de que seja identificado qual direção o olho
está apontando. Isso servirá para, num momento futuro, movimentar o mouse
na direção em que o olho aponta.

Num primeiro momento, as direções serão: cima, baixo, esquerda e direita.  
Quando uma maior experiência for desenvolvida na calibração do modelo,
as outras 4 direções referentes às diagonais serão adicionadas.

O **estado atual** do programa está marcado na *TODO list* abaixo. Por enquanto
os arquivos de imagem que servirão de entrada para a calibração do modelo
estão sendo salvos.

## *TODO list*

- [x] Identificação da face (visão)
- [x] Identificação dos olhos (visão)
- [x] Extração da imagem dos olhos para treinamento (visão)
- [ ] Pré-tratamento da imagem dos olhos antes do treinamento
  - [x] Aplicação de filtro *threshold* sobre a intensidade média da imagem (visão)
  - [ ] Normalização do tamanho (visão / aprendizado )
- [ ] Treinamento do modelo de predição (aprendizado)
- [ ] Execução do programa com o modelo calibrado (aprendizado)
- [ ] Predição satisfatória da direção do olho (aprendizado)
