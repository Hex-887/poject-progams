import math

#ввод данных
x = float(input("введите x:"))


#вычисление первого выражения
z1 = (1 + 2.5 * x) / (x ** 2 * (1 - x))

#вычисление второго выражения
z2 = math.sqrt(x) * math.sqrt(math.fabs(1-x)) * ((x ** 2 + 1) ** (1/3)) * ((math.fabs(math.sin(x))) ** (1/4))

#вычисление третьего выражения
Z3 = (math.sin(math.sqrt(x))) ** 3

#вычисление четвертого выражения
rad15 = math.sin(math.radians(15))
z4 = math.log10(1 + x) + math.log10(5) + math.cos(rad15)

#вычисление пятого выражения
z5 = math.exp(2) + math.exp(math.tan(x))

#вывод результатов
print("z1 = ", z1)
print("z2 = ", z2)
print("z3 = ", Z3)
print("z4 = ", z4)
print("z5 = ", z5)