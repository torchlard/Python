import numpy as np
import cv2

img = np.zeros((512,512,3), np.uint8)
cv2.line(img, (0,0),(511,511),(255,0,0),5)
cv2.rectangle(img, (384,0),(510,120),(0,255,0),3)
cv2.circle(img,(447,63),63,(0,0,255),-1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,250),font, 4, (255,255,255),5,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()
