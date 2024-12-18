# Giới thiệu về phân cụm FCM

## Phân cụm FCM là gì?
Phân cụm FCM (Fuzzy C-Means) là một phương pháp phân cụm dữ liệu dựa trên lý thuyết tập mờ, cho phép mỗi điểm dữ liệu thuộc về nhiều cụm với mức độ thành viên (**membership degree**) khác nhau. Mức độ này phản ánh khả năng hoặc xác suất điểm dữ liệu thuộc về các cụm.

## Hàm mục tiêu:
Hàm mục tiêu của FCM được sử dụng để tối ưu hóa mức độ thành viên \(u_{ik}\) và tâm cụm \(v_k\).  

### Tìm:
- **Mức độ thành viên**: \(u_{ik}\)  
- **Tâm cụm**: \(v_k\)

## Điều kiện:
- Ma trận mức độ thành viên \(u_{ik}\) phải thỏa mãn điều kiện:
  ![Screenshot 2024-12-17 212804](https://github.com/user-attachments/assets/e9b57a91-acb9-4e2b-85ae-a8f814598333)
)

---

## Thuật toán FCM:
1. **Khởi tạo** ma trận thành viên với kích thước \(N \times C\) (với \(N\) là số điểm dữ liệu và \(C\) là số cụm).
2. **Tính tâm cụm**:
   \[
   v_k = \frac{\sum_{i=1}^N u_{ik}^m \cdot x_i}{\sum_{i=1}^N u_{ik}^m}
   \]
3. **Cập nhật lại ma trận thành viên**:
   \[
   u_{ik} = \frac{1}{\sum_{j=1}^c \left( \frac{\|x_i - v_k\|}{\|x_i - v_j\|} \right)^{\frac{2}{m-1}}}
   \]
4. **Lặp lại** bước 2 và 3 cho đến khi hội tụ (chênh lệch giữa các lần lặp nhỏ hơn một ngưỡng).
5. **Gán nhãn** dựa trên mức độ thành viên lớn nhất.

---

## Ưu điểm:
- Cho phép một điểm dữ liệu thuộc về nhiều cụm với mức độ thành viên khác nhau.
- Phù hợp với dữ liệu phức tạp và có giao thoa giữa các cụm.

## Nhược điểm:
- Hiệu quả phụ thuộc vào số cụm \(c\) và tham số mờ \(m\).
- Dễ bị ảnh hưởng bởi các điểm bất thường (**outliers**).

---

## Ứng dụng:
- **Xử lý ảnh**
- **Khai thác dữ liệu**
- **Nhận dạng mẫu**
- **Phân tích thị trường**
- **Xây dựng hệ thống điều khiển mờ**
