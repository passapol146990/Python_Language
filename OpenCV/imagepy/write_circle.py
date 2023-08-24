import cv2
x0 = 1 #มีสี
img = cv2.imread('image/1.jpg',x0)

imgre = cv2.resize(img,(700,700))

cv2.circle(imgre,(290,300),50,(0,0,255),5)
cv2.circle(imgre,(550,550),40,(0,0,255),-1)

cv2.imshow('img',imgre)
cv2.waitKey(0)
cv2.destroyAllWindows()
