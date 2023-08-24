import cv2

img = cv2.imread('../1.jpg')
img = cv2.resize(img,(720,500))
imgG = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face = cv2.CascadeClassifier('../../haarcascades/haarcascade_frontalface_default.xml')
# face = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
# ตรงนี้ไม่ต้องกำหนดก็ได้ มีกำหนดเองอยู่แล้ว
scaleFactor = 1.04 #ขนาดใบหน้า 1.01-1.09 ยิ่งน้อยยิ่งไม่ค่อยแม่นแต่ตรงง่าย 
minNeighber = 5 #ตรงสอบใบหน้าตามรอบ ถ้า 5 คือตรวจสอบ 5 ครั้งว่าคือใบหน้าจริง แล้ววาดวงสี่เหลี่ยม
# จำแนกใบหน้าทีละ 1 คน
face_detect = face.detectMultiScale(imgG,scaleFactor,minNeighber)

for (x,y,w,h) in face_detect:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=5)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()