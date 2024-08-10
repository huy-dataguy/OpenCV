import cv2
import numpy as np

img = np.zeros((200, 200), dtype=np.uint8)

# Make a white square in the middle of the image
img[50:150, 50:150] = 255

# Apply a threshold to the image convert to binary
ret, thresh = cv2.threshold(img, 127, 255, 0)

# Find contours in the thresholded image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Convert the image to color so we can draw colored contours
color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

# Draw the found contours on the image in green
img = cv2.drawContours(color, contours, -1, (0, 255, 0), 2)

cv2.imshow("contours", color)

cv2.waitKey()
cv2.destroyAllWindows()
