import numpy as np
from numpy.linalg import eig
def PCA(A, k):
M = np.mean(A.T, axis=1)
C = A - M
V = np.cov(C.T)
values, vectors = eig(V)
idx = values.argsort()[::-1]
values = values[idx]
vectors = vectors[:, idx]
P = C.dot(vectors[:, :k])
return P
n, m = map(int, input("Enter shape of matrix: ").split())
print("Enter matrix: ")
A = np.array([i for _ in range(n) for i in map(int,
input().split())]).reshape(n, m)
k = int(input("Enter number of components to keep: "))
print(f"{k} principal component(s):\n", PCA(A, k))
