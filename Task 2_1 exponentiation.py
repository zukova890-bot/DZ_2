x = input("Введите числа через пробел: ").split()
p = input("Введите степень: ")

print(len(x))

if p.isdigit() or (p[0] == "-" and p[1:].isdigit()):
    p = int(p)
    result = []

    for i in x:
        if i.isdigit() or (i[0] == '-' and i[1:].isdigit()):
            result.append(str(int(i)**p))
        else:
            result.append(i*p)

    print("Вывод: ", ' '.join(result))
else:
    print("Ошибка: степень должна быть целым числом")


