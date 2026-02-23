l1 = input("Введите первый список: ")
a = l1.split()

l2 = input("Введите второй список: ")
b = l2.split()

common_set = set(a) & set(b)
common_list = list(common_set)
print("Общие элементы: ", " ".join(common_list))