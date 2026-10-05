q = float(input("Введите номер задания: "))
if q == 1:
    n = int(input())
    for i in range(n+1):
        print(i)

elif q == 2:
    total = 0
    for i in range(3):
        price = float(input())
        total = total + price
    print('Сумма введѐнных чисел равна', total)

elif q == 3:
    n = int(input())
    total = 0
    for i in range(n):
        print('Рассматриваем число', i)
        total += i
    print('Промежуточная сумма равна', total) 
    print('Итоговая сумма всех этих чисел равна', total)

elif q == 4:
    for i in range(1, 11):
        print(i) # выведет на отдельных строчках числа
                # от 1 (включительно) до 11 (не включительно)
    for i in range(1, 11, 2):
        print(i) # выведет (на отдельных строчках) 1, 3, 5, 7, 9
    for i in range(10, 0, -1):
        print(i) # выведет 10, 9, ..., 1

else:
    print("Неправильный номер задания")