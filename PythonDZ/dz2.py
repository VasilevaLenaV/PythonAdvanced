# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

from copy import copy


num = int(input('Задача 2. Введите число:\n'))

hexadecimal_sys = 16
res = []
numbers = '0123456789abcdef'
while abs(num) > 0:
    res.append(num % hexadecimal_sys)
    num = num // hexadecimal_sys

hexa_lst = []

for i in res:
    hexa_lst.append(numbers[i])
print(*hexa_lst[::-1], sep='')
check_num = hex(copy(num))
print(check_num)