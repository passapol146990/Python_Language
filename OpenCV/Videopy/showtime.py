import cv2,datetime
time = datetime.datetime.now()
cap = cv2.VideoCapture(0)

while True:
    check, frame = cap.read()
    time = datetime.datetime.now()
    cv2.putText(frame,str(time)[0:-5],(10,30),4,0.8,(255,255,255))
    cv2.imshow("output",frame)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

cap.release()
cv2.destroyAllWindows()
