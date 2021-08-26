import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('D:/face/dataFace.xml')
cap = cv2.VideoCapture(0)
data=[]
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        print(roi_color)
        print(roi_gray)
        if len(data) < 400:
             data.append(roi_color)
             data.append(roi_gray)
       
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff or len(data)>=200
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
np.save('temp',data)
