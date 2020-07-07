# reduzir ruido: abrir todas as imagens e fazer a média de cada pixel
import cv2
import numpy as np

# abrindo todas as imagens e armazenando na lista img[]
img = []
for i in range(9):
    filename = f'a{i+1}.jpg'
    print(filename)
    img.append(cv2.imread(filename))
    img[i] = img[i].astype('float64')

# somando todos os elementos de img[] item por item
# e guardando o resultado em soma
soma = sum(img)
# dividindo cada elemento de soma por 9 e guardando em avg (média)
avg = np.divide(soma, 9)
# convertendo de volta para uint8
avg = avg.astype('uint8')
# salvando imagem resultante
cv2.imwrite('average.jpg', avg)
