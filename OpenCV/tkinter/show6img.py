import matplotlib.pyplot as plt
import cv2

gray_img = cv2.imread('tkinter/01.png')

thresh,th1 = cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY)
thresh,th2 = cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY_INV)
thresh,th3 = cv2.threshold(gray_img,128,255,cv2.THRESH_TRUNC)
thresh,th4 = cv2.threshold(gray_img,128,255,cv2.THRESH_TOZERO)
thresh,th5 = cv2.threshold(gray_img,128,255,cv2.THRESH_TOZERO_INV)

images = [gray_img,th1,th2,th3,th4,th5]
titles = ["original",'binary','binary_inv','trunc','tozero','tozero_inv']

for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
