class Matrix:
    """
    Класс матрица.
    ...
    Атрибуты
    --------
    rows : int
        размер матрицы, кол-во строк матрицы
    cols : int
        размер матрицы, кол-во столбцов
    Методы
    ------
    __str__(self):
        Переводит матрицу в строку
    __eq__(self, other):
        Сравнивает матрицы по размеру и содержимому
    __add__(self, other):
        Складывает две матрицы при условии, что размеры равны
    __mul__(self, other):
        Умножает две матрицы при условии, что размеры равны
    """

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0] * cols for _ in range(rows)]

    def __str__(self):
        """Метод перевода матрицы в строку"""
        matrix_str = ""
        for row in self.matrix:
            matrix_str += " ".join(str(element) for element in row) + "\n"
        return matrix_str

    def __eq__(self, other):
        """Метод сравнения матриц"""
        if isinstance(other, Matrix) and self.rows == other.rows and self.cols == other.cols:
            return self.matrix == other.matrix
        return False

    def __add__(self, other):
        """Метод сложения матриц"""
        if isinstance(other, Matrix) and self.rows == other.rows and self.cols == other.cols:
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return result
        else:
            raise ValueError("Ошибка сложения, размеры матриц не совпадают")

    def __mul__(self, other):
        """Метод умножения матриц"""
        if isinstance(other, Matrix) and self.cols == other.rows:
            result = Matrix(self.rows, other.cols)
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(self.cols):
                        result.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return result
        else:
            raise ValueError("Ошибка умножения, размеры матрицы не совпадают")

