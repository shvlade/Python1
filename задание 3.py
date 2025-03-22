from math import factorial

n = int(input('Введите число n'))
a = n
while a  != 1:
    a = a - 1
    print(a,factorial(a))