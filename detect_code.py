import numpy as np
import cv2

disease_cascade=cv2.CascadeClassifier('cascade.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    disease = disease_cascade.detectMultiScale(gray, 1.3, 5)
    num=1
    
    # add this
    for (x,y,w,h) in disease:
        font=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,'spot'+str(num),(x-y,y-h),font,0.5,(0,255,255),2,cv2.LINE_AA)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        num+=1


    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        print(num)
        break


if num >= 1:
    print('diseased')
else :
    print('healthy')



cap.release()
cv2.destroyAllWindows()
