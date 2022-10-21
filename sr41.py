N = int(input("Ввод размера массива: "))
A = [0] * N
from random import randint
for i in range(N):
    A[i] = randint(-10, 10)
print("Входной массив: ", A)
MaxA = max(A)
for i in range(A.index(MaxA)+1, N):
    A[i] = 0
print("Результат массива: ", A)