import cv2
import numpy as np
img = cv2.imread('MyPic.png')
cv2.imwrite('hello.jpg', img)
cv2.imshow('my image', img)
cv2.waitKey()
cv2.destroyAllWindows()
