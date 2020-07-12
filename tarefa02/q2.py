import numpy as np
import cv2 as cv
import math


# retornando tamanho de kernel
def get_kernel(tam):
    lim_inf = math.floor(tam/2)
    lim_sup = math.ceil(tam/2)
    kernel = np.ones((tam,tam))
    kernel = kernel.astype('uint8')
    return kernel


# retorna uma amostra de dimensoes tam de uma matriz 
def get_amostra(src, y, x, tam):
    lim_inf = math.floor(tam/2)
    lim_sup = math.ceil(tam/2)
    amostra = src[y-lim_inf:y+lim_sup, x-lim_inf:x+lim_sup]
    amostra = amostra.astype('uint8')
    return amostra

# funcao de suavizacao de médias com kernel de tamanho tam variavel
# quanto maior tam, maior o efeito de 'blur'
# obs.: retorna imagem com bordas pretas
def smooth_fun(src, tam=3):
    lim_inf = math.floor(tam/2)
    lim_sup = math.ceil(tam/2)
    kernel = get_kernel(tam)
    smooth = np.zeros(src.shape)
    smooth = smooth.astype('uint8')
    rows, cols = src.shape
    for y in range(rows):
        for x in range(cols):
            if y > lim_inf and y < rows-lim_sup and x>lim_inf and x<cols-lim_sup:
                amostra = get_amostra(src, y, x, tam)
                soma = (kernel * amostra).sum()
                smooth[y, x] = soma / kernel.sum()
    return smooth


# afetando menos as bordas na suavização (detecçao de bordas pelo filtro laplaciano])
# só funciona com tamanho de kernel 3 (devido ao tamanho fixo do filtro laplaciano)
# quanto maior lim, mais a imagem se parece com a original
def smooth_fun_b(src, lim=100):
    tam=3
    lim_inf = math.floor(tam/2)
    lim_sup = math.ceil(tam/2)
    #kernel = np.ones((tam,tam))
    #kernel = kernel.astype('uint8')
    laplace = np.array([[1,1,1],[1,-8,1],[1,1,1]])
    laplace = laplace.astype('uint8')
    smooth = np.zeros(src.shape)
    smooth = smooth.astype('uint8')
    rows, cols = src.shape
    for y in range(rows):
        for x in range(cols):
            if y > lim_inf and y < rows-lim_sup and x>lim_inf and x<cols-lim_sup:
                amostra = get_amostra(src, y, x, tam)
                borda = abs((laplace * amostra).sum())
                if (borda > lim):
                    kernel = get_kernel(tam)
                    soma = (kernel * amostra).sum()
                    smooth[y,x] = soma / kernel.sum()
                else:
                    smooth[y, x] = src[y ,x]
    return smooth

### Fim das funções

original = cv.imread("image.jpg", 0);
stripes = cv.imread("stripes.jpg", 0);

# suavizando imagem com listras
stripes_smooth = smooth_fun(stripes, 7)

# suavizando imagem original
original_smooth = smooth_fun(original, tam=3)
# suzavizando imagens afetando menos as bordas
original_smooth_b = smooth_fun_b(original, lim=500)

# exibindo resultados
horizontal_img = np.concatenate((stripes, stripes_smooth), axis=1)
cv.imshow("", horizontal_img)
cv.waitKey()

horizontal_img = np.concatenate((original, original_smooth, original_smooth_b), axis=1)
cv.imshow("", horizontal_img)
cv.waitKey()