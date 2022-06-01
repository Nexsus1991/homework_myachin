from functools import reduce
from itertools import count, cycle

# Задание 1

# Файл my_script.py

# Задание 2

# list1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# list2 = [list1[i] for i in range(1, len(list1)) if list1[i] > list1[i - 1]]
# print(list2)

# Задание 3

# print([i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0])

# Задание 4

# my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# print([num for num in my_list if my_list.count(num) == 1])

# Задание 5

# def gen():
#     for i in range(100, 1001):
#         if i % 2 == 0:
#             yield i
# print(reduce(lambda x, y: x * y, gen()))

# Задание 6

# for el in count(3):
#     print(el)
#     if el >= 10:
#         break

# i = 0
# for el in cycle([1, 2, 3, 4, 5, 6, 7, 8, 9]):
#     print(el)
#     i += 1
#     if i == 9:
#         break

# Задание 7

# def fact(n):
#     el = 1
#     for i in range(1, n + 1):
#         el = el * i
#         yield print(f'!{i} = {el}')
# print([el for el in fact(int(input()))]) # Правда не совсем понимаю, почему у меня появляется список значений None


