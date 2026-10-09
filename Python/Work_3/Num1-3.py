import math as mt

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

elif select == 2:
    renge = input("Введите числа через запятую: ")
    result = []
    for i in renge:
        i_s = float(i)
        s = mt.sin(i_s)
        result.append(result)
    print(result)

elif select == 3:
    select2 = int(input("Номер формулы: "))
    if select2 == 1:
        a = int(input("Начало диапазона: "))
        print("Таблица для суммы F")
        print("i | значение выражения | сумма до | сумма после")

        F = 0

        for i in range(a, 21):
            expr = mt.sin(2*i + 2) / mt.cos(2*i)   # формула
            sum_before = F
            F += expr
            sum_after = F

            print(f"{i} | {expr:.6f} | {sum_before:.6f} | {sum_after:.6f}")

        print("\nИтоговая сумма F =", F)
    elif select2 == 2:
        a2 = int(input("Начало диапазона: "))
        x = int(input("x=: "))
        print("Таблица для произведения R")
        print("L | значение выражения | произведение до | произведение после")

        R_prod = 1

        for L in range(3, 16):
            expr = (mt.log(x * L) / 10000) + (1 / mt.tan(x))
            prod_before = R_prod
            R_prod *= expr
            prod_after = R_prod

            print(f"{L} | {expr:.6f} | {prod_before:.6f} | {prod_after:.6f}")

        R = 4 * x**2 + R_prod
        print("\nИтоговое значение R =", R)
    else:
        print("Некорректный номер формулы")