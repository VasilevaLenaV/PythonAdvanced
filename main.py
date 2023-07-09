# 1.Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
import os


def split_path(file_path):
    path, filename = os.path.split(file_path)
    name, extension = os.path.splitext(filename)
    return path, name, extension


result_path = os.path.abspath('main.py')
print(split_path(result_path))

# 2.Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%». В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

names = ["Иванов", "Петров", "Сидоров"]
rates = [100, 200, 300]
bonuses = ["10.25%", "15%", "5.5%"]

result_gen_dict = {name: rate * float(bonus.strip("%")) / 100 for name, rate, bonus in zip(names, rates, bonuses)}

print(result_gen_dict)


# 3.Создайте функцию генератор чисел Фибоначчи (см. Википедию)
def fibonacci_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fibonacci_ = fibonacci_gen()
for i in range(5):
    print(next(fibonacci_))
