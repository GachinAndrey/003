def my_degree(x, y):
    resalt = 1
    for i in range(abs(y)):
        resalt *= x
    if y >= 0:
        return resalt
    else:
        return 1 / resalt


print(my_degree(float(input("Введите положительное число X: ")),
                int(input("Введите отрицательную степень числа X: "))))
