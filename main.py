from task1 import MyString
from task2 import Archive
from dz2 import Matrix

my_str = MyString(4, 'Test task1')
print(my_str)
print(f"{my_str.value};{my_str.name};{my_str.init_time}")

arh = Archive(1, 'arh -1')
arh2 = Archive(2, 'arh -2')
arh3 = Archive(3, 'arh -3')
print(arh3)

print(repr(arh3))

matrix1 = Matrix(3, 3)
matrix1.matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(f"Матрица:\n{matrix1}")

matrix2 = Matrix(3, 3)
matrix2.matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Matrix.__eq__.__doc__)
print(matrix1 == matrix2)

matrix3 = matrix1 + matrix2
print(matrix3.__add__.__doc__)
print(matrix3)

matrix4 = matrix1 * matrix2
print(matrix4.__mul__.__doc__)
print(matrix4)

print(matrix1.__doc__)
