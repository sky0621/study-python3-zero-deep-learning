import numpy as np

X = np.array([[51,55],[14,19],[0,4]])
print(X)

print(X[0])
print(X[0][1])
print(X[2])
print(X[1][0])

X = X.flatten()
print(X)

print(X>15)

print(X[X>15])
