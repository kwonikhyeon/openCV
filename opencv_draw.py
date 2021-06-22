import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#print(img)
#img[:] = 255,200,200 #B G R 순 색깔구성
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,0,255),3)#shape:행렬의 크기
cv2.rectangle(img,(0,0),(250,350),(255,0,0),3)
cv2.circle(img,(200,150),50,(120,150,0),3)

cv2.imshow("img", img)
cv2.waitKey(0)