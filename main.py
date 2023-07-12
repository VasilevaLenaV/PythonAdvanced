from base_chess.chess import queen_will_beat_queen
from base_chess.chess import random_queen_arrangement
from base_chess.chess import prefill_queens
# 1.Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# prefill_auto = prefill_queens()
# queens_auto = []
# for x, y in enumerate(prefill_auto):
#     queens_auto.append((x, y))
#
# print(queen_will_beat_queen(queens_auto))

queens = []

for _ in range(8):
    x, y = map(int, input(f'Введите {_+1} пару чисел от 1 до 8, разделенных пробелом:').split())
    queens.append((x, y))

print(queen_will_beat_queen(queens))



# 2.Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в
# задаче выше. Проверяйте различные случайные варианты и выведите 4 успешных расстановки. *Выведите все успешные
# варианты расстановок

count = 0
for arrangement in random_queen_arrangement():
    print(arrangement)
    count += 1
    if count == 4:
        break
