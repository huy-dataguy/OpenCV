import cv2
videoCapture = cv2.VideoCapture('MyInputVid.avi')
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),


int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter('MyOutputVid.avi', cv2.VideoWriter_fourcc('I','4','2','0'),
 fps, size)

#cv2.VideoWriter_fourcc(('M','P','4','V'))
#cv2.VideoWriter_fourcc('X','2','6','4')
#.........vân vân   
# - Mã FourCC (Four Character Code), là các mã nhận dạng codec (các phương pháp nén video) cụ thể được sử dụng với OpenCV để ghi video
# - Các mã này giúp bạn lựa chọn codec phù hợp cho việc ghi video dựa trên yêu cầu về kích thước tệp, chất lượng video và khả năng tương thích


success, frame = videoCapture.read()
while success: # Loop until there are no more frames.
    videoWriter.write(frame)
    success, frame = videoCapture.read()