a = {'один': 1, 'два': 2, 'три': 3, }
x = iter(a.items())
print(x)
y = next(x)
print(y)
z = next(iter(y))
print(z)