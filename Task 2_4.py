x = input("Введите строку: ")
a = x.lower().split()
uni_world = set(a)

for i in uni_world:
    count = a.count(i)
    print(f"{i}: {count}")