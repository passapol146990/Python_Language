import cv2
x0 = 1 #มีสี
img = cv2.imread('image/1.jpg',x0)

imgre = cv2.resize(img,(700,700))
# putRwxt(ภาพ,ข้อความ,พิกัด,ฟอนมขนาดมสีมความหนา)
cv2.putText(imgre,'PASSAPOl',(150,150),5,1.8,(0,0,255),cv2.LINE_4)

cv2.imshow('img',imgre)
cv2.waitKey(0)
cv2.destroyAllWindows()
