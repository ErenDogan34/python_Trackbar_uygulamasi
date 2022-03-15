import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

def degisim(x):
    img = np.zeros((512, 512, 3), np.uint8)
    cv2.circle(img,(256,256),100,(255,0,0),x)
    cv2.imshow("photo",img)



cv2.imshow("photo",img)
cv2.createTrackbar("degisim","photo",1,15,degisim)
cv2.waitKey()