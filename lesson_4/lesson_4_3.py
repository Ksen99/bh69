a = input("name: ")
b = input("email: ")
some_dict = {
    "name": a,
    "email": b,
}
w = int(input("n: "))
some_list = {i: some_dict.keys() for i, some_dict.keys() in range(0, w+1)}
print(some_list)