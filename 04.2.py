def my_degree(x, y):
    if x == 0:
        return 0
    elif y == 0:
        return 1
    elif y == 1:
        return x
    elif y < 0:
        return 1 / (x * my_degree(x, -y - 1))
    else:
        return x * my_degree(x, y - 1)


print(my_degree(float(input("Введите положительное число X: ")),
                int(input("Введите отрицательную степень числа X: "))))
