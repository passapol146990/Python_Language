import cv2,matplotlib.pyplot as plt

def display():
    pass

cv2.namedWindow("threshold")
cv2.createTrackbar("value","threshold",128,255,display)
img = cv2.imread('tkinter/1.jpg',0)
img = cv2.resize(img,(720,500))
while True:
    
    thresh_value = cv2.getTrackbarPos("value","threshold")
    thresh,result = cv2.threshold(img,thresh_value,255,cv2.THRESH_BINARY) #ดำเป็นขาว
    thresh,result = cv2.threshold(img,thresh_value,255,cv2.THRESH_BINARY_INV) #ขาวเป็นดำ

    if cv2.waitKey(1)& 0xFF == ord('e'):
        break
    cv2.imshow('threshold',result)

cv2.destroyAllWindows()