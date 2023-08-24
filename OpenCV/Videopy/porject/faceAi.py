import cv2

cap = cv2.VideoCapture(0)
face = cv2.CascadeClassifier('../../haarcascades/haarcascade_frontalface_default.xml')

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face_delect = face.detectMultiScale(gray,1.1,3)
    for (x,y,w,h) in face_delect:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=5)
        cv2.imshow('video',frame)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break


cap.release()
cv2.destroyAllWindows()


