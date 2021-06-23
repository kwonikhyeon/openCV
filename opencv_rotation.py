import cv2
import numpy as np

img = cv2.imread('resources/card.jpg')
img = cv2.resize(img, dsize=(640, 480), interpolation=cv2.INTER_AREA)#이미지크기

width,height = 350,250

pts1 = np.float32([[26,115],[78,329],[259,46],[304,241]])
pts2 = np.float32([[0,0],[0,height],[width,0],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)#투시변환
imgOutput = cv2.warpPerspective(img,matrix,(width,height))#투시변환 적용

cv2.imshow("Image",img)
cv2.imshow("OutPutImage",imgOutput)

cv2.waitKey(0) #출력대기시간