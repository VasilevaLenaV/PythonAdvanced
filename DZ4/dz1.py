# Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s (кроме переменной из одной буквы s) на None.
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

apples = 5
bananas = 10
oranges = 3
fruit = 123
s = "Hello"


def replace_():
    global_ =globals()
    var_without_ = {}

    for name, value in global_.items():
        if name.endswith("s") and len(name) > 1:
            global_[name] = None
            new_var_name = name[:-1]
            var_without_[new_var_name] = value

    return var_without_


def main():
    variables = replace_()

    print(apples)
    print(bananas)
    print(oranges)
    print(s)
    print(variables)
