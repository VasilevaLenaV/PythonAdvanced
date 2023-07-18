# Нахождение корней квадратного уравнения
def validate_input(func):
    def wrapper(a, b, c):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
            raise ValueError("Коэффициенты должны быть числами")
        return func(a, b, c)
    return wrapper


def calculate_roots(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        return "Нет действительных корней"


@validate_input
def find_roots(a, b, c):
    roots = calculate_roots(a, b, c)
    if isinstance(roots, tuple):
        print(f"Действительные корни: {roots[0]}, {roots[1]}")
    else:
        print(roots)