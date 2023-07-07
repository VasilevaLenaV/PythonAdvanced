# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def get_dict(**kwargs):
    res = {}
    for key, value in kwargs.items():
        if not isinstance(key, (int, float, str, tuple, frozenset)):
            key = str(key)
        res[value] = key
    return res


def main():
    result = get_dict(apple="fruit", banana="fruit", carrot="vegetable", tomato="fruit")
    print(result)
