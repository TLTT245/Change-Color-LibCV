import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
points = []

cap.release()
cv.destroyAllWindows()

cap = cv.VideoCapture(0)

# Định nghĩa HSV range cho 7 màu cầu vồng
color_ranges = {
    "red":    [(np.array([0,120,70]),  np.array([10,255,255])),
               (np.array([170,120,70]), np.array([180,255,255]))], # đỏ có 2 khoảng
    "orange": [(np.array([11,100,100]), np.array([25,255,255]))],
    "yellow": [(np.array([26,100,100]), np.array([35,255,255]))],
    "green":  [(np.array([36,100,100]), np.array([85,255,255]))],
    "blue":   [(np.array([86,100,100]), np.array([125,255,255]))],
    "indigo": [(np.array([126,100,100]), np.array([140,255,255]))], # lam
    "violet": [(np.array([141,100,100]), np.array([160,255,255]))]  # tím
}

# --- Nhập màu bạn muốn tracking ---
selected_color = input("Nhập tên màu (red, orange, yellow, green, blue, indigo, violet): ").strip().lower()

if selected_color not in color_ranges:
    print("Màu không hợp lệ!")
    cap.release()
    cv.destroyAllWindows()
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Tạo mask cho màu đã chọn
    mask_total = np.zeros(hsv.shape[:2], dtype=np.uint8)
    for (lower, upper) in color_ranges[selected_color]:
        mask_total = cv.bitwise_or(mask_total, cv.inRange(hsv, lower, upper))

    contours, _ = cv.findContours(mask_total, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    direction = "No object"

    if contours:
        c = max(contours, key=cv.contourArea)
        (x, y), radius = cv.minEnclosingCircle(c)
        if radius > 15:
            if x < frame.shape[1]//3:
                direction = "LEFT"
            elif x > 2*frame.shape[1]//3:
                direction = "RIGHT"
            else:
                direction = "CENTER"

    cv.putText(frame, f"Direction: {direction}", (30, 50),
               cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)

    cv.imshow("Control by Color", frame)
    if cv.waitKey(1) & 0xFF == 27:  # Esc để thoát
        break

cap.release()
cv.destroyAllWindows()