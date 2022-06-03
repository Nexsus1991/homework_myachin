from sys import argv

path, time, rate, bonus = argv
time, rate, bonus = map(int, argv[1:])
salary = (time * rate) + bonus
print(salary)