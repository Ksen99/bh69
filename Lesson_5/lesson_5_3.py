# Вывести четные числа от 2 до N по 5 в строку
n = int(input())
a =[i for i in range(2, n) if i % 2 == 0]
if len(a) > 5:
    print(a)