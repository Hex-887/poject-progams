import math as mt
import sympy as sp

select = float(input("Введите номер задания "))

if select == 1:
    positive_sum = 0
    negative_sum = 0

    while True:
        num = int(input("Введите число: "))

        if num == 0:
            break

        if num > 0:
            positive_sum += num
        else:
            negative_sum += num

    print("Сумма положительных чисел:", positive_sum)
    print("Сумма отрицательных чисел:", negative_sum)

elif select == 1.1:
    print("Введите числа, чтобы закончить введите 0 или enter")
    summ = 0
    for i in summ:
        a = int(input())
        if a >= 0:
            summ += a
        else:
            break

elif select == 2:
    x = 0
    while (1 >= x >= 0):
        x = int(input(""))
        s = mt.sin(x)
        print(s)