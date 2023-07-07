# Напишите функцию для транспонирования матрицы
def transpose_(matrix):
    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed


def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transposed_ = transpose_(matrix)
    print(transposed_)
