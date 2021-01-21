def my_func(arg1, arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg2 < arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3


print(f'Сумма наибольших аргументов: {my_func(int(input("enter arg1: ")), int(input("enter arg2: ")), int(input("enter arg3: ")))}')
