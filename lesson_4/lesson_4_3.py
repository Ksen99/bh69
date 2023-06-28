a = input("name: ")
b = input("email: ")
some_dict = {
    "name": a,
    "email": b,
}
w = int(input("n: "))
some_list = {i: some_dict for i, some_dict in range(0, w+1)}
print(some_list)