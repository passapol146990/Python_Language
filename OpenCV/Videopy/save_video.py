import cv2
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')

result = cv2.VideoWriter('output.avi',fourcc,30.0,(640,480))

while cap.isOpened():
    check,frame  = cap.read()

    if check == True:
        cv2.imshow('output',frame)
        result.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('e'):
            break

result.release()
cap.release()
cv2.destroyAllWindows()