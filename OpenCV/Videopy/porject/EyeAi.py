import cv2

cap = cv2.VideoCapture(0)
eye = cv2.CascadeClassifier('../../haarcascades/haarcascade_eye_tree_eyeglasses.xml')
face = cv2.CascadeClassifier('../../haarcascades/haarcascade_frontalface_default.xml')

while True:
    _, frame = cap.read()
    grayFace,grayEye = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY),cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face_delect,eye_delect = face.detectMultiScale(grayFace,1.1,3),eye.detectMultiScale(grayEye,1.1,3)
    
    for x1,y1,w1,h1 in face_delect:
        cv2.rectangle(frame,(x1,y1),(x1+w1,y1+h1),(0,255,0),thickness=5)
        for (x2,y2,w2,h2) in eye_delect:
            cv2.rectangle(frame,(x2,y2),(x2+w2,y2+h2),(0,255,0),thickness=5)
        cv2.imshow('video',frame)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break


cap.release()
cv2.destroyAllWindows()


