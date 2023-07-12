n = int(input("Введите число: "))
f = 0
a = 1
print(f, a, end=" ")
while n > 2:
    f, a = a, f + a
    print(a, end=" ")
    n -= 1

