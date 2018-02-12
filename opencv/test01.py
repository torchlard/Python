import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('brick.jpg',1)
cv2.imshow('image',img)
k = cv2.waitKey(0) & 0xFF
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('messigray.jpg',img)
    cv2.destroyAllWindows()

# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.xticks([]), plt.yticks([])
# plt.show()

