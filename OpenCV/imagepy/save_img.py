import cv2
x0 = 1 #มีสี
img = cv2.imread('1.jpg',x0)

imgre = cv2.resize(img,(400,400))

cv2.imshow('img',imgre)
cv2.imwrite('export.png',imgre)

cv2.waitKey(0)
cv2.destroyAllWindows()
