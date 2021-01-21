def my_func():
    try:
        number1 = float(input("Введите делимое: "))
        number2 = float(input("Введите делитель: "))
        resalt = number1 / number2
    except ValueError:
        return 'Введено не число!'
    except ZeroDivisionError:
        return "Вы не можете делить на ноль!"

    return resalt


print(f'Результат {my_func()}')

