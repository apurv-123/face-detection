import cv2
import time

face_cascade = cv2.CascadeClassifier('D:/face-detection/dataFace.xml')
eye_cascade = cv2.CascadeClassifier('D:/face-detection/dataEyes.xml')

eye_flage=True
show_count=True
blink_count=0

cap = cv2.VideoCapture(0)

while True:
    ret, img=cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        eye_flage=False
        img=cv2.rectangle(img, (x,y), (x+w,y+h), (256,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            eye_flage=True
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            
            
    if eye_flage:
        show_count=True
        
    if show_count and not (eye_flage):
        show_count=True
        blink_count+=1
        
    font=cv2.FONT_HERSHEY_PLAIN
    cv2.putText(img, 'blink count->='+ str(blink_count) , (25,50), font,2, (0,0,0),2)
    
    cv2.imshow('Apurv',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
cap.release()
cv2.destroyAllWindows()
            