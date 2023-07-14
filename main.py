
import os.path

from base_serialization.serialization import read_csv
from base_serialization.serialization import csv_to_pickle
from base_serialization.serialization import pickle_to_csv
from base_serialization.serialization import csv_to_dict
from base_serialization.serialization import dict_to_pickle_file
from base_serialization.serialization import read_csv_dr
from base_serialization.serialization import get_folder_info

filename_ = 'biostats_tab.csv'

# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. Распечатайте его как pickle строку.
task0 = read_csv(filename_)
print(csv_to_pickle(task0))

# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
task1 = csv_to_dict(filename_)
dict_to_pickle_file(task1, 'task1_dict')
pickle_to_csv('task1_dict.pickle', 'task1_dict.csv')

# csv.DictReader. Распечатайте его как pickle строку.
task2 = read_csv_dr(filename_)
print(csv_to_pickle(task2))

# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# -Для дочерних объектов указывайте родительскую директорию.
# -Для каждого объекта укажите файл это или директория.
# -Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

get_folder_info(os.path.curdir, os.path.curdir + '/serial/')

