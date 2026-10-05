a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a == b:
    if a == c:
        print ("Все числа равны")
    else:
        print ("a=b")
else:
    if a == c:
        print ("a=c")
    else:
        if b == c:
            print ("b=c")
        else:
            print ("Все числа различны")

if a < b:
    if a < c:
        y = a
    else:
        y = c
else:
    if b < c:
        y = b
    else:
        y = c

print ("Минимальное число" , y)