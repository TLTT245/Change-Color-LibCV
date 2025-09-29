import cv2 as cv
flags = [i for i in dir(cv) if i.startswith('COLOR_')]
print( flags )

import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0, cv.CAP_DSHOW)  
while(1):
    # Lấy từng khung hình
    _, frame = cap.read()
    # Chuyển đổi BGR sang HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # xác định phạm vi màu xanh lam trong HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    # Ngưỡng hình ảnh HSV để chỉ có màu xanh lam
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # Mặt nạ Bitwise-AND và hình ảnh gốc
    res = cv.bitwise_and(frame,frame, mask= mask)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()

green = np.uint8([[[0,255,0 ]]])
hsv_green = cv.cvtColor(green,cv.COLOR_BGR2HSV)
print( hsv_green )