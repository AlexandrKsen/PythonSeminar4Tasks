# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

numN = int(input("Введите натуральное число: "))

if numN <= 0:
    print("Введенное знаечение не является натуральным числом")

for i in range(1, numN+1):
    if (numN % i == 0):
        print(i)
