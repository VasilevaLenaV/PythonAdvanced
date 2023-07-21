from animal import Factory
from serialization import SerializationFactory

# 1 Доработаем задачи 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

animal = Factory.get("Cat", name="Barsik", color="Black")
animal.speak()

animal = Factory.get('Bird', name="Paprika")
animal.speak()

animal = Factory.get("Fish", name="Nemo")
animal.speak()

animal = Factory.get("Dog", name="Reks")
animal.speak()

# 2 Возьмите 1-3 любые задачи из прошлых семинаров, которые вы уже решали. Превратите функции в методы класса.
# Задачи должны решаться через вызов методов экземпляра.

dirinfo = SerializationFactory()
dirinfo.folder_info()
dirinfo.export_json()