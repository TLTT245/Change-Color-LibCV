# Computer Vision - Changing Colorspaces & Color Tracking

## 📌 Giới thiệu
Repo này chứa 2 chương trình Python sử dụng **OpenCV** để làm việc với không gian màu (Colorspaces) và **theo dõi vật thể theo màu sắc** từ webcam.  
Đây là bài thực hành trong môn **Computer Vision**.

---

## 🚀 Yêu cầu
- Python 3.x  
- OpenCV (`pip install opencv-python`)  
- NumPy (`pip install numpy`)  
- Webcam để chạy demo

---

## 📂 Nội dung

### 1. `SourceCode.py`
- Mở webcam và chuyển đổi từ không gian màu **BGR → HSV**.  
- Tạo **mask cho màu xanh dương** và hiển thị:  
  - `frame` : ảnh gốc từ webcam  
  - `mask`  : vùng ảnh đã lọc theo màu xanh  
  - `res`   : kết quả sau khi lọc (bitwise AND)  
- In ra mã HSV của màu **xanh lá cây (green)** để tham khảo.

👉 Đây là ví dụ **cơ bản nhất** của việc thay đổi hệ màu và lọc 1 màu cụ thể trong ảnh.

---

### 2. `Changecoloropen.py`
- Mở webcam và cho phép người dùng **nhập màu muốn theo dõi** (red, orange, yellow, green, blue, indigo, violet).  
- Xác định **HSV range** cho 7 màu cầu vồng.  
- Tìm contour của vật thể có màu đó, vẽ **hình tròn bao quanh** và xác định **vị trí theo chiều ngang**:
  - LEFT  
  - CENTER  
  - RIGHT  
- Hiển thị hướng trên khung hình (`Direction: ...`).

👉 Đây là ví dụ **nâng cao**, cho phép theo dõi nhiều màu khác nhau chứ không chỉ một màu cố định.

---

## 📷 Demo
- Khi đưa vật thể màu xanh dương vào camera với `SourceCode.py`, chỉ phần màu xanh được giữ lại.  
- Khi chạy `Changecoloropen.py` và nhập `red`, camera sẽ theo dõi vật thể màu đỏ và báo hướng **LEFT / CENTER / RIGHT**.

---

## 📝 Ghi chú
- Nhấn **Esc** để thoát chương trình.  
- Có thể thay đổi ngưỡng HSV để phù hợp với điều kiện ánh sáng thực tế.  
- Đây là code phục vụ học tập và demo, có thể mở rộng thêm:  
  - Tracking nhiều vật thể cùng lúc.  
  - Vẽ quỹ đạo di chuyển.  
  - Ứng dụng trong điều khiển bằng màu sắc.

---
