import numpy as np
import pandas as pd
from scipy.spatial.distance import cdist

class FCM():
    def __init__(self,c=2,m=2,max_iter=1000,epsilon=1e-5):
        self.c=c #số tâm cụm
        self.m=m #tham số mờ hóa
        self.max_iter=max_iter #số vòng lặp tối đa
        self.epsilon=epsilon #ngưỡng hội tụ dừng vòng lặp
        self.tamcum=None #tâm cụm (sẽ được cập nhật trong quá trình lặp)
        self.U=None #ma trận thành viên

    #khởi tạo ma trận thành viên
    def khoi_tao_matrix_U(self,n):
        U=np.random.rand(n,self.c) #tạo ma trận ngẫu nhiên [n,c]
        U=U/np.sum(U,axis=1,keepdims=True) #chuẩn hóa mỗi hàng tổng = 1
        return U
    
    #tính tâm cụm
    def tinhtamcum(self,data):
        u_m=self.U**self.m #tính ma trận u_m
        tamcum=np.dot(u_m.T,data)/np.sum(u_m.T,axis=1,keepdims=True)
        return tamcum #[c,d]

    #cập nhật lại ma trận thành viên U
    def cap_nhat_U(self,data):

        D=[]
        for j in range(self.c):
            #tính khoảng cách từng điểm dữ liệu đến tâm cụm thứ j
            distane_ij=cdist(data,self.tamcum[j][np.newaxis,:])**(2/(self.m-1)) 
            D.append(distane_ij) #[c,n]
        TS=1/np.array(D)
        MS=np.sum(1/np.array(D), axis=0)
        U=TS/MS #[c,n]
        U = np.squeeze(U).T #[n,c] 
        return U
        
    #chạy thuật toán FCM
    def fit(self,data):
        n=data.shape[0] 
        self.U=self.khoi_tao_matrix_U(n)
        for i in range(self.max_iter):
            U_old=self.U.copy() #Lưu lại ma trận U của lần lặp trước để kiểm tra hội tụ

            self.tamcum=self.tinhtamcum(data) #cập nhật tâm cụm 

            self.U=self.cap_nhat_U(data) #cập nhật lại ma trận U

            #Kiểm tra điều kiện hội tụ dựa trên sự thay đổi của ma trận U
            if np.linalg.norm(self.U - U_old) < self.epsilon:
                print(f"Hội tụ sau {i+1} lần lặp")
                break

        return self.U,self.tamcum

    #Gán label cho từng điểm dữ liệu
    def predict(self):
        return np.argmax(self.U,axis=1)

if __name__=="__main__":

    df=pd.read_csv('Real estate.csv')
    data=df.values
    
    dulieu=FCM(c=3,m=2,max_iter=1000,epsilon=1e-5)

    U,tamcum=dulieu.fit(data)

    print('Tâm cụm:')
    print(tamcum)

    print('Ma trận thành viên:')
    print(U)

    labels=dulieu.predict()
    print(labels)
