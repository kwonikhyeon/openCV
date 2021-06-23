import cv2
import numpy as np

def getContours(img):
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>100:
            cv2.drawContours(imgContour,cnt,-1,(0,255,0),1)


cap = cv2.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)

print('width :%d, height : %d' % (cap.get(3), cap.get(4)))

while True:
    success, img = cap.read()
    flip_img = cv2.flip(img,1)
    imgContour = img.copy()  # findContours함수는 원본이미지를 변경시키기 때문에 복사본 사용

    if(success):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(21,21),0)
        canny = cv2.Canny(img,100,100)
        getContours(canny)
        cv2.imshow("video", img)
        cv2.imshow("ContourImage", imgContour)
        '''
        cv2.imshow("flip_video", flip_img)
        cv2.imshow("canny_video", canny)
        cv2.imshow("gray_video", gray)
        '''
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break