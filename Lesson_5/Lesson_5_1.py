number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
a = number_1 * number_2 + number_3
for i in range(number_3, a):
    if i % number_2 == 0:
       print(i)
