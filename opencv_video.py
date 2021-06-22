import cv2


cap = cv2.VideoCapture("resources/test_video.mp4")

cap.set(3,640)
cap.set(4,480)

print('width :%d, height : %d' % (cap.get(3), cap.get(4)))

while True:
    success, img = cap.read()
    img = cv2.flip(img,1)
    if(success):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(21,21),0)
        canny = cv2.Canny(img,50,50)
        cv2.imshow("canny_video", canny)
        cv2.imshow("gray_video", gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break