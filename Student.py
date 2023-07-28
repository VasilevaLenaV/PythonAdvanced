# Создайте класс студента.
# * Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# * Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# * Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# * Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

import csv
import re


class FioDescriptor:
    def check_fio(self, value):
        for val in re.split(";|,|\n| ", value):
            if not val.isalpha():
                return False
        return True

    def __get__(self, instance, owner):
        return instance._fio

    def __set__(self, instance, value):
        if not isinstance(value, str) or not self.check_fio(value) or not value.istitle():
            raise ValueError("Не верный формат ФИО")
        instance._name = value


class ItemDescriptor:
    def __get__(self, instance, owner):
        return instance._items

    def __set__(self, instance, value):
        if not isinstance(value, list):
            raise ValueError("Предмет не содержится в списке")
        instance._items = value


class Student:
    fio = FioDescriptor()
    items = ItemDescriptor()

    def __init__(self, name, file_items):
        self.fio = name
        self.load_items(file_items)
        self.scores = {item: {"grades": [], "test_results": []} for item in self.items}

    def item_err(self,item):
        return f"Предмет {item} не найден"

    def load_items(self, file_items):
        with open(file_items, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            self.items = next(reader)

    def add_score(self, item, grade, test_result):
        if item not in self.items:
            raise ValueError(self.item_err(item))
        if grade not in range(2, 6):
            raise ValueError("Ошибка значения. Оценка должна быть в диапазоне от 2 до 5")
        if test_result not in range(101):
            raise ValueError("Ошибка значения. Результат теста должен быть в диапазоне от 0 до 100")

        self.scores[item]["grades"].append(grade)
        self.scores[item]["test_results"].append(test_result)

    def average_grade(self, item):
        if item not in self.items:
            raise ValueError(self.item_err(item))

        grades = self.scores[item]["grades"]
        if len(grades) == 0:
            return 0

        return sum(grades) / len(grades)

    def print_average(self):
        result = ""
        for item in self.items:
            result += f"Тест по {item}, средний балл: {self.average_test_result(item)}\n"

        return result

    def average_test_result(self, item):
        if item not in self.items:
            raise ValueError(self.item_err(item))

        test_results = self.scores[item]["test_results"]
        if len(test_results) == 0:
            return 0

        return sum(test_results) / len(test_results)

    def overall_average_grade(self):
        all_grades = []
        for item in self.items:
            all_grades.extend(self.scores[item]["grades"])
        if len(all_grades) == 0:
            return 0

        return sum(all_grades) / len(all_grades)

    def print_overall_average(self):
        return f"Средний балл по оценкам всех предметов вместе взятых: {self.overall_average_grade()}"
