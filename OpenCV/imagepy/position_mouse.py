import cv2
x0 = 1 #มีสี
x1 = 0 #ขาวดำ
img = cv2.imread('image/1.jpg',x0)


def showPosition(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        text = str(x)+','+str(y)
        cv2.putText(imgre,text,(x,y),4,0.3,(0,0,255))
        cv2.imshow('img',imgre)
imgre = cv2.resize(img,(500,500))


cv2.imshow('img',imgre)
cv2.setMouseCallback('img',showPosition)


cv2.waitKey(0)
cv2.destroyAllWindows()
