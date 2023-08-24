import cv2,numpy
title = '1.jpg'

img = cv2.imread(title)
imgre = cv2.resize(img,(780,500))

points = []

def clickposition(even,x,y,flags,param):
    if even == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(imgre,(x,y),10,(0,0,255),1)
        points.append((x,y))
        if len(points)>=2:
            cv2.line(imgre,points[-2],points[-1],(0,255,0),5)
        cv2.imshow(title,imgre)

cv2.imshow(title,imgre)
cv2.setMouseCallback(title,clickposition)
cv2.waitKey(0)
cv2.destroyAllWindows()

