import cv2 as cv

img = cv.imread('img.jpg')
cv.imwrite('canny.png', cv.Canny(img, 200, 400))
cv.imshow('canny', cv.imread('canny.png'))
cv.waitKey()
cv.destroyAllWindows()