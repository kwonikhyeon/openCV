import cv2
import numpy as np

def getContours(img):
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)#폐곡선의 영역
        print(area)
        if area>500:
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)#윤곽선 길
            print(peri)



img = cv2.imread('resources/shapes.jpg')
img = cv2.resize(img, dsize=(640, 480), interpolation=cv2.INTER_AREA)#이미지크기
imgContour = img.copy()#findContours함수는 원본이미지를 변경시키기 때문에 복사본 사용

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,100,100)

getContours(imgCanny)

#imgHor = np.hstack((img,img))#수평연결
#imgVer = np.vstack((img,img))#수직연결

#cv2.imshow("H",imgHor)
#cv2.imshow("V",imgVer)

cv2.imshow("OriginalImage",img)
cv2.imshow("GrayImage",imgGray)
cv2.imshow("BlurImage",imgBlur)
cv2.imshow("CannyImage",imgCanny)
cv2.imshow("ContourImage",imgContour)

cv2.waitKey(0) #출력대기시간