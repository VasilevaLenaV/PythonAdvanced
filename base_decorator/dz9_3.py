import csv
import math


# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
def quadratic_equation_solver(func):
    def wrapper(file_name):
        with open(file_name, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                a, b, c = map(int, row)
                result = func(a, b, c)
                print(f"Корни квадратного уравнения {a}x^2 + {b}x + {c}:")
                print(f"Корень 1: {result[0]}")
                print(f"Корень 2: {result[1]}")
                print()

    return wrapper


@quadratic_equation_solver
def find_roots_quadratic(a, b, c):
    discriminant = b * b - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root, root
    else:
        return None, None
