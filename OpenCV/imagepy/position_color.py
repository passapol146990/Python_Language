import cv2,numpy
title = '1.jpg'

img = cv2.imread(title)
imgre = cv2.resize(img,(780,500))

def clickColor(even,x,y,flags,param):
    if even == cv2.EVENT_LBUTTONDOWN:
        blue = imgre[y,x,0]
        green = imgre[y,x,1]
        red = imgre[y,x,2]

        text = str(blue) +','+ str(green) +','+ str(red)
        cv2.putText(imgre,text,(x,y),5,0.8,(0,0,255))
        cv2.imshow(title,imgre)

def clickNewcolor(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = imgre[y,x,0]
        green = imgre[y,x,1]
        red = imgre[y,x,2]

        imgcolor = numpy.zeros([300,300,3],numpy.uint8)
        imgcolor[:] = [blue,green,red]
        cv2.imshow('color',imgcolor)


cv2.imshow(title,imgre)
# cv2.setMouseCallback(title,clickColor)
cv2.setMouseCallback(title,clickNewcolor)
cv2.waitKey(0)
cv2.destroyAllWindows()

