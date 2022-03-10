import numpy as np


A = np.array([[2,5],
              [1,3],
              [4,1]])

B = np.array([[4,-1],
              [2,3],
              [6,2]])

C = np.array([[1,2,2],
              [3,4,5]])

BC = np.dot(B,C)
CA = np.dot(C,A)

print("(a) A + B = \n", A+B)
print("(b) B - A = \n", B-A)
print("(c) BC = \n", BC)
print("(d) CA = \n", CA)
