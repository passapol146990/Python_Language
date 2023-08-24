import cv2
x0 = 1 #มีสี
img = cv2.imread('image/1.jpg',x0)

imgre = cv2.resize(img,(700,700))

cv2.line(imgre,(10,10),(500,10),(255,0,0),10) #เส้นตรงสีฟ้า
cv2.arrowedLine(imgre,(100,100),(500,100),(255,0,0),10) #ลูกศรตรงสีฟ้า

cv2.imshow('img',imgre)
cv2.waitKey(0)
cv2.destroyAllWindows()
