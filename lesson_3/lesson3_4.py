# Задача 4
a = int(input("number_1: "))
b = int(input("number_2: "))
c = int(input("number_3: "))
v = int(a >= 0)
g = int(b >= 0)
z = int(c >= 0)
f = 3 - v - g - z
p = 3 - f
print("Положительных - ", p, "отрицательных -", f)