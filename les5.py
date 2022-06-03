import random
import re
import json

# Задание 1

# with open('Задание1.txt', 'a') as f:
#     while True:
#         name = input('Name: ')
#         age = input('Age: ')
#         empty = ''
#         if not name or not age:
#             break
#         else:
#             f.writelines(f'Hello, {name}\nYour age: {age}\n {empty}\n')

# Задание 2

# count = 0
# with open('Задание2.txt', 'r') as f:
#     while True:
#         i = f.readline()
#         count += 1
#         if count <= 3:
#             words = len(i.split(' '))
#             print(f'Количество слов в {count}-ой строке = {words}')
#         else:
#             break
#     print(f'Количество строк: {count - 1}') # С костылями, но работает :)

# Задание 3

# salary = 0
# count = 0
# with open('Задание3.txt', 'r') as f:
#     while True:
#          i = f.readline()
#          if not i:
#              break
#          else:
#              name = i.split()
#              if int(name[1]) <= 20000:
#                  print(name[0])
#              salary = int(name[1]) + salary
#              count += 1
#     print(f'Средняя зп сотрудников = {int(salary / count)}')

# Задание 4

# with open('Задание4.txt', 'r') as f:
#     while True:
#         i = f.readline()
#         if not i:
#             break
#         else:
#             stroka = i.split()
#             if stroka[0] == 'One':
#                 stroka[0] = 'Один'
#                 with open('Задание4_1.txt', 'a') as d:
#                     d.write(' '.join(stroka) + '\n')
#             elif stroka[0] == 'Two':
#                 stroka[0] = 'Два'
#                 with open('Задание4_1.txt', 'a') as d:
#                     d.write(' '.join(stroka) + '\n')
#             elif stroka[0] == 'Three':
#                 stroka[0] = 'Три'
#                 with open('Задание4_1.txt', 'a') as d:
#                     d.write(' '.join(stroka) + '\n')
#             elif stroka[0] == 'Four':
#                 stroka[0] = 'Четыре'
#                 with open('Задание4_1.txt', 'a') as d:
#                     d.write(' '.join(stroka) + '\n')
# создал монстра Владимира, но IT'S ALIVE!!! :)

# Задание 5

# with open('Задание5.txt', 'w') as f:
#     count = 1
#     my_sum = 0
#     while count <= 10:
#         num = random.randrange(1, 10)
#         my_list = str(num) + ' '
#         count += 1
#         my_sum = my_sum + num
#         f.write(my_list)
#     f.write(f'Сумма = {str(my_sum)}')

# Задание 6

# with open('Задание6.txt', 'r') as f:
#     my_dict = {}
#     while True:
#         i = f.readline()
#         if not i:
#             break
#         else:
#             res = re.findall(r'\d+', i)
#             res2 = int(res[0]) + int(res[1]) + int(res[2])
#             name = i.split(':')[0]
#             my_dict2 = {name: res2}
#             my_dict = my_dict | my_dict2
#     print(my_dict)

# Задание 7

with open('Задание7.txt', 'r', encoding='utf-8') as f:
    average_profit = 0
    my_dict = {}
    while True:
        i = f.readline()
        if not i:
            break
        else:
            num = re.findall(r'\d+', i)
            profit = int(num[0]) - int(num[1])
            name = i.split(',')[0]
            my_dict2 = {name: profit}
            my_dict = my_dict | my_dict2
            if profit > 0:
                average_profit = average_profit + profit
        average_profit_dict = {'average_profit': average_profit}
    my_list = [my_dict, average_profit_dict]
with open('Задание7.json', 'w', encoding='utf-8') as f:
    json.dump(my_list, f, indent=2, ensure_ascii=False)