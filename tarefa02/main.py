import cv2 as cv
import numpy as np

img = cv.imread("image.jpg", 0);

# aumenta o brilho
brighter = np.zeros(img.shape)
brighter = brighter.astype('uint8')
for (y,x), value in np.ndenumerate(img):
    brighter[y,x] = min(255, 60 + value);

# adiciona linhas
stripes = np.copy(brighter)
stripes = stripes.astype('uint8')
rows = img.shape[0]
cols = img.shape[1]
for y in range(rows):
    count = 0
    for x in range(cols):
        if count > 2 and count < 8:
            stripes[y,x] = 0
        elif count > 4:
            count = 0
        count += 1


# concatenando imagens (matrizes) em uma linha
horizontal_img = np.concatenate((img, brighter, stripes), axis=1)
cv.imshow("", horizontal_img)
cv.waitKey()