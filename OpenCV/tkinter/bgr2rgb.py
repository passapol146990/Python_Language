import matplotlib.pyplot as plt
import cv2

img = cv2.imread('tkinter/1.jpg')
imgre = cv2.resize(img,(400,400))
cv2.imshow('img',imgre)

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()
