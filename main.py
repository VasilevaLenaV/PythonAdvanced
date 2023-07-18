from base_decorator import find_roots
from base_decorator import test_function
from base_decorator import find_roots_quadratic
from base_decorator import gen_random_numbers

# * Нахождение корней квадратного уравнения
find_roots(1, -2, 1)
# * Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
gen_random_numbers('numbers.csv')
# * Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
find_roots_quadratic('numbers.csv')
# * Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
test_function(10, 5)

