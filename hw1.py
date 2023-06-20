# Таблица умножения, как в тетрадке

def block1(a, b):
    for y in range(2, 11):
        for x in range(a, b):
            block2(x, y)
        print('')
    print('')


def block2(a, b):
    max_width = 2
    print(f'{a:{max_width}}  * {b:{max_width}} = {a * b:{max_width}}\t\t', end='')


def main():
    title = str.upper('Таблица умножения')
    print(f'\n{title.center(80)}\n')
    block1(2, 6)
    block1(6, 10)


main()