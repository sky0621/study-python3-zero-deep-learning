import numpy as np


A = np.array([[1, 2], [3, 4]])
print("＜要素A＞")
print(A)

print("各次元の要素数")
print(A.shape)

print("配列要素のデータ型")
print(A.dtype)

print(" ")
print("＜要素B＞")
B = np.array([[3, 0], [0, 6]])
print(B)

print("各次元の要素数")
print(B.shape)

print("配列要素のデータ型")
print(B.dtype)

print(" ")
print("A + B")
print(A+B)
print("A - B")
print(A-B)
print("A * B")
print(A*B)
print("A / B")
print(A/B)

print("A * 10")
print(A*10)
