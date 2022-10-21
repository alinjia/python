SzN = int(input("Введите размер массива N: "))
A = [0] * SzN
SzM = int(input("Введите размер массива M: "))
B = [0] * SzM
from random import randint
for i in range(SzN):
    A[i] = randint(0, 10)
print(A)
for j in range(SzM):
    B[j] = randint(0, 10)
print(B)
C = []
for a in A:
    if a in B:
        C.append(a)
print(C)