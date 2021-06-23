import cv2

faceCascade = cv2.CascadeClassifier("resources/haarcascade_frontalface_default.xml")
font = cv2.FONT_HERSHEY_SIMPLEX

cap = cv2.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)

print('width :%d, height : %d' % (cap.get(3), cap.get(4)))

while True:
    success, img = cap.read()
    flip_img = cv2.flip(img,1)

    if(success):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.putText(img, 'Faces', (x - 5, y - 5), font, 0.5, (255, 255, 255), 1)

        cv2.imshow("video", img)
        #cv2.imshow("flip_video", flip_img)
        #cv2.imshow("gray_video", gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break