import numpy as np
import cv2 as cv
import math

stripes = cv.imread("stripes.jpg", 0);


# funcao de suavizacao
# por enquanto funciona pra kernel 3x3
# tentando implementar qualquer kernel ímpar (3, 5, 7, ...)
def smooth_fun(src, y, x, tam=3):
    kernel = np.array([[1,2,1],[2,4,2],[1,2,1]])    # falta calcular kernel para tam > 3
    kernel = kernel.astype('uint8')
    inf_lim = math.floor(tam/2)
    sup_lim = inf_lim + 1
    amostra = src[y-inf_lim:y + sup_lim, x - inf_lim:x + sup_lim]
    soma = kernel * amostra
    return soma.sum() / kernel.sum()

# suavizando imagem
smooth = np.zeros(stripes.shape)
smooth = smooth.astype('uint8')
rows, cols = stripes.shape
for y in range(rows):
    for x in range(cols):
        if y > 1 and y < rows-2 and x>1 and x<cols-2:
            smooth[y,x] = smooth_fun(stripes, y, x)


horizontal_img = np.concatenate((stripes, smooth), axis=1)
cv.imshow("", horizontal_img)
cv.waitKey()