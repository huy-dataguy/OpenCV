import cv2
import numpy as np

# Check the OpenCV version
OPENCV_MAJOR_VERSION = int(cv2.__version__.split('.')[0])

# Load and downscale the image
img = cv2.pyrDown(cv2.imread("hammer.png"))

# Convert to grayscale and apply threshold
ret, thresh = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                            127, 255, cv2.THRESH_BINARY)

# Find contours based on OpenCV version
if OPENCV_MAJOR_VERSION >= 4:
    contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                                      cv2.CHAIN_APPROX_SIMPLE)
else:
    _, contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                                         cv2.CHAIN_APPROX_SIMPLE)

# Iterate through contours and draw bounding shapes
for c in contours:
    # Find bounding box coordinates
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Find minimum area rectangle
    rect = cv2.minAreaRect(c)

    # Calculate coordinates of the minimum area rectangle
    box = cv2.boxPoints(rect)

    # Normalize coordinates to integers using int32 or int64
    box = np.int32(box)

    # Draw contours of the minimum area rectangle
    cv2.drawContours(img, [box], 0, (0, 0, 255), 3)

    # Calculate center and radius of the minimum enclosing circle
    (x, y), radius = cv2.minEnclosingCircle(c)

    # Cast to integers
    center = (int(x), int(y))
    radius = int(radius)

    # Draw the circle
    img = cv2.circle(img, center, radius, (0, 255, 0), 2)

# Draw all contours
cv2.drawContours(img, contours, -1, (255, 0, 0), 1)

# Display the image with contours
cv2.imshow("contours", img)
cv2.waitKey()
cv2.destroyAllWindows()
