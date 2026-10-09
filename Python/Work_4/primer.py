select = int(input("Выберите номер примера: "))

if select == 1:
    i = 1
    while i <= 10:
        print(i ** 2)
        i += 1

elif select == 2:
    n = int(input())
    leght = 0
    while n > 0:
        n //= 10
        leght += 1
    print(leght)

elif select == 3:
    number = int(input("Число для факториала: "))
    i = 1
    factorial = 1
    while 1 <= number:
        factorial *= i
        i += 1
    print ("Факториал числа", number, "равен", factorial)
    
elif select == 4:
    select2 = int(input("Ревизия задания: "))
    if select2 == 1:
        a = int(input())
        while a != 0:
            if a < 0:
                print("Встретилось отрицательное число", a)
                break
            a = int(input())
        else:
            print("Ни одного отрицательного числа не встретилось")
    elif select2 == 2:
        a2 = input("Введите числа через запятую: ")
        # разбиваем строку на список строк
        parts = a2.split(",")

        for p in parts:
            p = p.strip()       # убираем пробелы
            a = float(p)        # превращаем строку в число

            if a < 0:
             print("Встретились отрицательные числа:", a)
             break
            else:
             print("Число положительное:", a)

elif select == 5:
    import random

    number = random.randint(0, 100)
    attempts = 0   # счётчик попыток

    while True:
        answer = input('Угадай число: ')

        if answer == "" or answer == "exit":
           print("Выход из программы")
           break

        if not answer.isdigit():
           print("Введи правильное число")
           continue

        answer = int(answer)
        attempts += 1   # увеличиваем счётчик на каждой попытке

        if answer == number:
           print(f'Верно! Ты угадал за {attempts} попыток.')
           break
        elif answer > number:
           print('Загаданное число меньше')
        else:
           print('Загаданное число больше')
