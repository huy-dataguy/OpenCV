import cv2 as cv

captureVid = cv.VideoCapture(0)
# Đặt FPS và kích thước khung hình phù hợp với tốc độ của camera
fps = 30

# Nếu camera chỉ có thể đạt được 30 FPS thay vì 120 FPS như bạn đặt,
#  việc ghi video sẽ lâu hơn vì phải ghi nhiều khung hình hơn mà camera có thể cung cấp

size = (int(captureVid.get(cv.CAP_PROP_FRAME_WIDTH)), int(captureVid.get(cv.CAP_PROP_FRAME_HEIGHT)))

capVidOut = cv.VideoWriter('out.avi', cv.VideoWriter_fourcc('I','4','2','0'), fps, size)

numFrameRemain =10  * fps -1

success, frame = captureVid.read()

while(success and numFrameRemain > 0):
    capVidOut.write(frame)
    numFrameRemain-=1
    success, frame = captureVid.read()
