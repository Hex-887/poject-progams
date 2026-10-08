print("Введите числа. Чтобы закончить, введите 0")

numbers = []   # здесь будет наш массив

# цикл ввода значений
while True:
    a = float(input())
    if a == 0:
        break
    numbers.append(a)   # добавляем в массив

# теперь можно обработать массив через for
positive_sum = 0
negative_sum = 0

raid = []

for num in numbers:
    if num in range(1, 3):
        raid.append(num)
    else:
        continue

print("Принадлежат массиву: ", raid)

