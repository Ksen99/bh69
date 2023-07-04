number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))
a = input("Выберите знак (+, -, *, /, %): ")
if a == "+":
    print(number_1 + number_2)
elif a == "-":
    print(number_1 - number_2)
elif a == "*":
    print(number_1 * number_2)
elif a == "/":
    print(number_1 / number_2)
elif a == "%":
    print(number_1 % number_2)
else:
    print("Введено неверное значение")