import cv2,numpy
while True:
    img = cv2.imread('color.png')
    img = cv2.resize(img,(400,400))

    lower = numpy.array([5,111,10])
    upper = numpy.array([124,255,133])

    mask = cv2.inRange(img,lower,upper)
    result = cv2.bitwise_and(img,img,mask=mask)
    if cv2.waitKey(0) & 0xFF == ord('e'):
        break
    cv2.imshow('color',img)
    cv2.imshow('Mask',mask)
    cv2.imshow('result',result)

cv2.destroyAllWindows()




