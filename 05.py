def my_sum():
    sum_res = 0
    ext = False
    while not ext:
        number = input('Введите числа через пробел или Q для выхода: ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ext = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Текущая сумма: {sum_res}')
    print(f'Сумма: {sum_res}')


my_sum()
