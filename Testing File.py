import numpy as np
A = np.array([[8,2,3],[1,6,3],[1,3,3]])
b = np.array([1,7,3])
print(A)
x = np.linalg.solve(A,b)
print(x)