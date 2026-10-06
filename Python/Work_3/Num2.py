import math as mt
import sympy as sp

select = float(input("Введите номер задания "))

if select == 1:
    n = 1
    for i in range(n + 1):
        print ("Введите числа, для окончания введите 0")
        y = input("")

        if not y == 0:
            y += i
        