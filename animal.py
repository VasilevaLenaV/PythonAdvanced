# Доработаем задачи 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
from typing import Callable


class Factory(object):
    @staticmethod
    def get(class_name: str, **kwargs) -> object:
        if type(class_name) != str:
            raise ValueError("class_name must be a string!")

        raw_subclasses_ = AnimalFactory.__subclasses__()
        classes: dict[str, Callable[..., object]] = {c.__name__: c for c in raw_subclasses_}
        class_ = classes.get(class_name, None)
        if class_ is not None:
            return class_(**kwargs)

        raise ValueError(f"Unsupported animal type: {class_name}")


class AnimalFactory(object):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} says {self.voice}")


# Пример классов животных
class Bird(AnimalFactory):
    def __init__(self, name):
        self.voice = 'Chick-Chirico!'
        self.name = name


class Fish(AnimalFactory):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} not says 'Bool-bool-bool!, i am fish")


class Cat(AnimalFactory):
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.voice = 'Meow!'

    def speak(self):
        print(f"{self.color} {self.name} says {self.voice}")


class Dog(AnimalFactory):
    def __init__(self, name):
        self.name = name
        self.voice = 'Woof!'
