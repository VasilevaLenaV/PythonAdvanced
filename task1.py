# Задание №1
# Создайте класс Моя Строка, где:
# -будут доступны все возможности str
# -дополнительно хранятся имя автора строки и время создания (time.time)


from time import strftime, gmtime, time


class MyString(str):
    """
        Класс Моя Строка.
        ...
        Атрибуты
        --------
        value : int
            Значение
        name : str
            Имя автора строки
        Методы
        ------
        __new__(cls, value, name):
            Метод возвращает экземпляр класса с атрибутами
        __str__(self):
            Метод возвращает строковое значение атрибута value
        """
    def __init__(self, value, name):
        self.name = name
        self.value = value

    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        instance.init_time = strftime('%H:%M:%S', gmtime(time()))
        return instance

    def __str__(self):
        return str({'value': self})
