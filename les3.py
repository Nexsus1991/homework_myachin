# Задание 1

def my_div():
    try:
        arg1 = float(input('Укажите число а: '))
        arg2 = float(input('Укажите число b: '))
    except ValueError:
        return print('Похоже, что вы ввели не число')
    try:
        div = arg1 / arg2
    except ZeroDivisionError:
        return print('Уф, боюсь, поделить на ноль не выйдет')
    return div
print(my_div())

# Задание 2

def my_user():
    name = input('Имя: ')
    surname = input('Фамилия: ')
    birth = input('Год рождения: ')
    city = input('Город проживания: ')
    email = input('Электронная почта: ')
    phone = input('Телефон: ')
    x = [name, surname, birth, city, email, phone]
    return ' '.join(x)
print(my_user())

# Задание 3

def my_func(arg1, arg2, arg3):
    if (arg1 + arg3) < (arg1 + arg2) > (arg2 + arg3):
        return arg1 + arg2
    elif (arg1 + arg2) < (arg1 + arg3) > (arg2 + arg3):
        return arg1 + arg3
    elif (arg1 + arg2) < (arg2 + arg3) > (arg1 + arg3):
        return arg2 + arg3
print(my_func(int(input('Первый аргумент: ')), int(input('Второй аргумент: ')), int(input('Третий аргумент: '))))
# Снова громоздко, но работает

# Задание 4

def my_func(x, y): # 1
    return x ** y
print(my_func(float(input()), int(input())))

def my_func(x, y): # 2
    count = 1
    inc_x = x
    inc_x2 = x
    while count < abs(y) or y == 0:
        if y < 0:
            inc_x2 = inc_x2 * x
            inc_x = 1 / inc_x2
            count += 1
        elif y > 0:
            inc_x = inc_x * x
            count += 1
        elif y == 0:
            inc_x = 1
            return inc_x
    else:
        return inc_x
print(my_func(float(input()), int(input())))

# Задание 5

def my_func():
    a = 0
    while True:
        x = list(input('Введите числа через пробел: ').split())
        for i in x:
            if i == 'стоп':
                return print('Вы завершили процесс')
        y = [int(z) for z in x]
        a = a + sum(y)
        print(a)
print(my_func()) # пока идет трудновато. При завершении функция возвращает None, но я не могу понять - почему.

# Задание 6 и 7

def int_func():
    s = input()
    return s.title()
print(int_func())