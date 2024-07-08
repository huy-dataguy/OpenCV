import cv2

# Biến toàn cục để lưu trữ các vùng chọn
rectangles = []
cropping = False
current_rectangle = []

def click_and_crop(event, x, y, flags, param):
    global current_rectangle, cropping

    # Nếu nhấp chuột trái, bắt đầu chọn vùng
    if event == cv2.EVENT_LBUTTONDOWN:
        current_rectangle = [(x, y)]
        cropping = True

    # Nếu kéo chuột, cập nhật tọa độ vùng chọn
    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping:
            image_copy = image.copy()
            for rect in rectangles:
                cv2.rectangle(image_copy, rect[0], rect[1], (0, 255, 0), 2)
            cv2.rectangle(image_copy, current_rectangle[0], (x, y), (0, 255, 0), 2)
            cv2.imshow("image", image_copy)

    # Nếu nhả chuột trái, kết thúc chọn vùng
    elif event == cv2.EVENT_LBUTTONUP:
        current_rectangle.append((x, y))
        cropping = False
        # Chuẩn hóa tọa độ vùng chọn
        x1, y1 = current_rectangle[0]
        x2, y2 = current_rectangle[1]
        rect_normalized = [(min(x1, x2), min(y1, y2)), (max(x1, x2), max(y1, y2))]
        rectangles.append(rect_normalized)
        for rect in rectangles:
            cv2.rectangle(image, rect[0], rect[1], (0, 255, 0), 2)
        cv2.imshow("image", image)

# Tải ảnh
image_path = "test.png"
image = cv2.imread(image_path)
clone = image.copy()

cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)

# Hiển thị ảnh và chờ người dùng chọn vùng
while True:
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF

    # Nếu nhấn 'r', reset lại ảnh
    if key == ord("r"):
        image = clone.copy()
        rectangles = []

    # Nếu nhấn 'c', thoát vòng lặp
    elif key == ord("c"):
        break

# Áp dụng làm mờ cho tất cả các vùng chọn
for rect in rectangles:
    if rect[0][1] < rect[1][1] and rect[0][0] < rect[1][0]:  # Kiểm tra vùng chọn hợp lệ
        roi = clone[rect[0][1]:rect[1][1], rect[0][0]:rect[1][0]]
        if roi.size > 0:  # Đảm bảo vùng chọn không rỗng
            roi_blurred = cv2.GaussianBlur(roi, (51, 51), 0)
            clone[rect[0][1]:rect[1][1], rect[0][0]:rect[1][0]] = roi_blurred

# Hiển thị ảnh kết quả
cv2.imshow("blurred", clone)
cv2.waitKey(0)

# Lưu ảnh kết quả
output_path = "ans.png"
cv2.imwrite(output_path, clone)

cv2.destroyAllWindows()

output_path
