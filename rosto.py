import cv2

img = cv2.imread('pessoas.png')

cv2.imwrite('pessoas.png', img)
cv2.imshow('Imagem', img)
cv2.waitKey(0)
cv2.destroyAllWindows()