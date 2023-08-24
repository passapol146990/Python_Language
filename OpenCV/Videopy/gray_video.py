import cv2
cap = cv2.VideoCapture('video.mp4')

while cap.isOpen():
    check, frame = cap.read()
    if check == True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BAYER_BG2GRAY)
        cv2.imshow("output",frame)
        if cv2.waitKey(1) & 0xFF == ord('e'):
            print(ord('e'))
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
