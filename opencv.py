import cv2
import numpy as np

kernal = np.ones((3,3),np.uint8)

img = cv2.imread('resources/photo.png')
img = cv2.resize(img, dsize=(640, 480), interpolation=cv2.INTER_AREA)#이미지크기

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(15,15),0)#(홀수,홀수)
imgCanny = cv2.Canny(img,100,100)
imgDialation = cv2.dilate(imgCanny,kernal,iterations=1)#선 확장
imgEroded = cv2.erode(imgDialation,kernal,iterations=1)#선 침식

#cv2.imshow("output",img)
cv2.imshow("Gray",imgGray)
#cv2.imshow("Blur",imgBlur)
cv2.imshow("Canny",imgCanny)
cv2.imshow("Dialation",imgDialation)
cv2.imshow("Eroded",imgEroded)


cv2.waitKey(0) #출력대기시간

