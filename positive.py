import cv2
import os

i=1
for filename in os.listdir('itsp images'):
    img=cv2.imread(os.path.join('itsp images',filename))
    resized=cv2.resize(img,(50,50))
    cv2.imwrite(str(i)+".jpg", resized)
    i+=1
