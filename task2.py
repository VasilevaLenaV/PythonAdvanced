# Задание №2
# Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# При создании нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов
# list-архивы также являются свойствами экземпляра

class Archive:
    """
        Класс матрица.
        ...
        Атрибуты
        --------
        num : int
            Число
        value : str
            Строка
        Методы
        ------
        __new__(cls, *args):
            Метод возвращает новый экземпляр класса
        __str__(self):
            Метод представления экземпляра для пользователя
        __repr__(self):
            Метод представления экземпляра для программиста
        """
    _instance = None

    def __new__(cls, *args):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive = []
        else:
            cls._instance.archive.append({cls._instance.num,cls._instance.value})
        return cls._instance

    def __init__(self, num, value):
        self.num = num
        self.value = value

    def __str__(self):
        return f'{self.num}, {self.value}, {self.archive}'

    def __repr__(self):
        return f"Archive({self.num},'{self.value}')"


