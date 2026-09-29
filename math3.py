import numpy as np

A = np.array([
    [1, 2],
    [1, 3]
], dtype=float)

B = np.array([
    [3, 2],
    [2, 2]
], dtype=float)

A_inv = np.linalg.inv(A)
B_inv = np.linalg.inv(B)

AB = A @ B

left = np.linalg.inv(AB)

right = B_inv @ A_inv

np.set_printoptions(precision=3, suppress=True)

print("A^-1 =")
print(A_inv)

print("\nB^-1 =")
print(B_inv)

print("\nAB =")
print(AB)

print("\n(AB)^-1 =")
print(left)

print("\nB^-1 A^-1 =")
print(right)

print("\n(AB)^-1 = B^-1 A^-1 인가?")
print(np.allclose(left, right))