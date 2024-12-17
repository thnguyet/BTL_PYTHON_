import numpy as np
import pandas as pd

class LinearRegression():
    def __init__(self):
        self.weights=None #trọng số w
    
    #tính trọng số w theo công thức hồi quy tuyến tính
    def tinh_weights(self,X,y):
        X_bias = np.hstack([np.ones((X.shape[0], 1)), X])
        self.weights=np.linalg.pinv(X_bias.T @ X_bias) @ X_bias.T @ y

    #dự đoán kết quả
    def predict(self,X):
        X_bias = np.hstack([np.ones((X.shape[0], 1)), X])
        return X_bias @ self.weights
    
    def mse(self,y_true,y_pred):
        mse=np.mean((y_true-y_pred)**2)
        return mse
    
def xulydulieu(df):
    df=df.copy()
    X=df.drop(columns=['Y house price of unit area']).values
    y=df['Y house price of unit area'].values
    return X,y    

if __name__=="__main__":
    df=pd.read_csv('C:\\Users\\ADMIN\\Downloads\\Real estate.csv')
    
    X,y=xulydulieu(df)

    train_size = int(0.7 * len(X))  # 70% train, 30% test
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]
    print(train_size)
    dulieu=LinearRegression()

    dulieu.tinh_weights(X_train,y_train)
    print(dulieu.weights)

    y_pred = dulieu.predict(X_test)
    print("Giá trị dự đoán:", y_pred)

    mse = dulieu.mse(y_test, y_pred)
    print("Mean Squared Error (MSE):", mse)