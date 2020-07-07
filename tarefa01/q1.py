import cv2
import sys

# armazenando a imagem em uma matriz 
img = cv2.imread(sys.argv[1])
# verificando dimensoes da matriz
print(img.shape)

# separando os canais RGB utilizando array slicing
img_r = img[0:, 0:, 0:1]
img_g = img[0:, 0:, 1:2]
img_b = img[0:, 0:, 2:3]
# verificando dimensoes das matrizes resultantes
print(img_r.shape)
print(img_g.shape)
print(img_b.shape)

# escrevendo em arquivos de canais separados
cv2.imwrite('image_r.jpg', img_r)
cv2.imwrite('image_g.jpg', img_g)
cv2.imwrite('image_b.jpg', img_b)

cv2.imshow("r", img_r)
cv2.imshow("g", img_g)
cv2.imshow("b", img_b)

cv2.waitKey()