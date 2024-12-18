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


---

## Thuật toán FCM:
1. **Khởi tạo** ma trận thành viên với kích thước NxC (với \(N\) là số điểm dữ liệu và \(C\) là số cụm).
2. **Tính tâm cụm**:
   ![Screenshot 2024-12-17 213907](https://github.com/user-attachments/assets/b9f544b1-1605-45b4-a939-d29a2c74e5a6)

3. **Cập nhật lại ma trận thành viên**:
   ![Screenshot 2024-12-17 214943](https://github.com/user-attachments/assets/65886350-8c06-4749-b0a3-1aae422ea043)

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


# Giới thiệu về thuật toán Linear Regression

## Linear Regression là gì?
Linear Regression là một thuật toán học máy thuộc nhóm học có giám sát (**Supervised Learning**).  
Mục đích của giải thuật hồi quy tuyến tính là dự đoán giá trị của một hoặc nhiều biến mục tiêu liên tục (**continuous target variable**) \(y\) dựa trên một véc-tơ đầu vào \(\mathbf{x}\).

---

## Thuật toán

### **1. Mô hình:**  
Hồi quy tuyến tính mô hình hóa mối quan hệ giữa biến đầu vào và biến mục tiêu bằng phương trình:
![Screenshot 2024-12-18 101554](https://github.com/user-attachments/assets/d6b6fdfc-940a-438a-b9c2-e3b6c8cdbc02)

Hoặc dưới dạng vector:
![Screenshot 2024-12-18 102155](https://github.com/user-attachments/assets/53fa350c-f7cb-4f7b-a4f0-9c1011c40999)
 
Trong đó:
- \(y\): giá trị dự đoán
- \(\mathbf{X}\): ma trận đầu vào (kích thước \(N \times (n+1)\), bao gồm cả cột hệ số chặn 1)
- \(\mathbf{w}\): vector trọng số (bao gồm cả \(w_0\))

---

### **2. Sai số dự đoán:**  
Sai số dự đoán thể hiện sự chênh lệch giữa giá trị thực tế \(y_i\) và giá trị dự đoán \(\hat{y}_i\):
![Screenshot 2024-12-17 230838](https://github.com/user-attachments/assets/842cf467-f71f-4acf-a9aa-a104f1f84fc9)
 
Mục tiêu là làm cho sai số này **càng nhỏ càng tốt**.

---

### **3. Hàm mất mát:**  
Hàm mất mát phổ biến nhất là **Mean Squared Error (MSE)**, được định nghĩa:
![Screenshot 2024-12-18 110822](https://github.com/user-attachments/assets/7f6561db-6756-45e3-bf33-672d59d389e2)

Trong đó:
- \(N\): số lượng mẫu dữ liệu
- \(y_i\): giá trị thực tế
- \(\hat{y}_i\): giá trị dự đoán

---

### **4. Mục tiêu:**  
Tìm giá trị vector trọng số \(\mathbf{w}\) sao cho hàm mất mát nhỏ nhất:
\[
\min_{\mathbf{w}} \text{MSE}
\]
