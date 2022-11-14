import cv2
import numpy as np
img = cv2.imread("dog.jpg", cv2.IMREAD_GRAYSCALE)

kernelX = np.array([[1,1,1], [0,0,0], [-1,-1,-1]])
kernelY = np.array([-1,0,1], [1,0,1], [1,0,1])
PrewittX = cv2.filter2D(img, -1, kernelX)
PrewittY = cv2.filter2D(img, -1, kernelY)

SobelX = cv2.Sobel(img, cv2.cv_64F, 1, 0)
SobelY = cv2.Sobel(img, cv2.cv_64F, 0, 1)

img_canny = cv2.Canny(img,100,200)

cv2.imshow('original image', img)
cv2.imshow('PrewittX', PrewittX)
cv2.imshow('PrewittY', PrewittY)
cv2.imshow('Prewitt', PrewittX+PrewittY)
cv2.imshow('SobelX', SobelX)
cv2.imshow('SobelY', SobelY)
cv2.imshow('Sobel', SobelX+SobelY)
cv2.imshow('canny', img_canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
