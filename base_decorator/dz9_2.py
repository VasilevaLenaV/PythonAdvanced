import csv
import random


# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
def generate_csv_file(func):
    def wrapper(file_name):
        with open(file_name, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            func(writer)

    return wrapper


@generate_csv_file
def gen_random_numbers(writer):
    for _ in range(random.randint(100, 1000)):
        numbers = [random.randint(1, 100) for _ in range(3)]
        writer.writerow(numbers)
