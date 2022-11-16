import cv2

orig_img=cv2.imread("dog.jpg")
grey_img=cv2.cvtColor(orig_img, cv2.COLOR.BGR2GRAY)
cv2.inshow('color', orig_img)
cv2.inshow('grey', grey_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#img = QImage(self.image, w, h, line_len, QImage.Format_Grayscale8)
#8 bit dönüşüm için

#img = QImage(self.image, w, h, line_len, QImage.Format_Grayscale16)
#16 bit dönüşüm için
