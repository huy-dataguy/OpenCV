import cv2 as cv
clicked = False
vidCap = cv.VideoCapture(0)
def OnMouse(event, x, y, flags, param):
    global clicked 
    if event == cv.EVENT_LBUTTONUP:
        clicked = True


success, frame = vidCap.read()
cv.namedWindow('My camera')

# Gán hàm OnMouse làm hàm xử lý sự kiện chuột cho cửa sổ 'My camera'. 
# Bất cứ khi nào sự kiện chuột xảy ra trong cửa sổ này, hàm OnMouse sẽ được gọi.
cv.setMouseCallback('My camera', OnMouse)
#note: 
# setMouseCallback should take five arguments,
#Vì vậy dù các tham số trong hàm OnMouse không sử dụng, nhưng vẫn cần phải có để  setMouseCallback đủ 5 tham số
#Các tham số kia không gì thì mặc định giá trị sẽ bằng 0

while success and cv.waitKey(1) == -1 and not clicked :
    cv.imshow('My camera', frame)
    success, frame = vidCap.read()
cv.destroyAllWindows('My camera')
vidCap.release()