# Задание 1

result_list = ['hi', 34, 2.5, True, None]
for el in result_list:
    print(type(el))

# Задание 2

li = list(input('Заполните список: '))
for i in range(0, len(li) - 1, 2): # Здесь до меня долго не доходило, что надо len(li) - 1 вместо len(li)
    li[i], li[i + 1] = li[i + 1], li[i]
print(li)

# Задание 3

seasons = {'Зима': [1, 2, 12], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
month = int(input('Введите месяц: '))
for el in seasons:
    if month in seasons[el]:
        print(el)

seasons = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
month = int(input('Введите месяц: '))
for i in range(0, 2):
    if month == i + 1 or month == i + 12:
        print('Зима')
for i in range(2, 5):
    if month == i + 1:
        print('Весна')
for i in range(5, 8):
    if month == i + 1:
        print('Лето')
for i in range(8, 11):
    if month == i + 1:
        print('Осень')

# Задание 4

y = input('Ввод: ').split()
for ind, el in enumerate(y, 1):
    print(ind, el[0:10])

# Задание 5

my_list = [7, 5, 3, 3, 2]
x = int(input('Ввод: '))
for y in my_list:
    if x >= y:
        my_list.insert(my_list.index(y), x)
        print(my_list)
        break
    elif x == 0 or x == 1:
        my_list.insert(5, x)
        print(my_list)
        break

# Задание 6

x = 1
my_list = []
while x <= 3:
    name = input('Название: ')
    price = int(input('Цена: '))
    amount = int(input('Количество: '))
    unit = input('Единица измерения: ')
    my_dict = {'Название': name, 'Цена': price, 'Количество': amount, 'Ед': unit}
    my_list = my_list + [my_dict]
    x += 1
for i in enumerate(my_list, 1):
    print(list(i))
# Вторую часть не осилил. Полагаю, что для этого нужно первую часть писать иначе.
