import os
import json
import csv
import pickle


# 3. Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# -Для дочерних объектов указывайте родительскую директорию.
# -Для каждого объекта укажите файл это или директория.
# -Для файлов сохраните его размер в байтах,
# а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

def get_folder_info(directory_path, output_folder):
    directory_info = []
    size_dict = {}

    for root, dirs, files in os.walk(directory_path):
        size = sum(os.path.getsize(os.path.join(root, file)) for file in files)
        size += sum(size_dict.get(os.path.join(root, d), 0) for d in dirs)

        # Информация о текущей директории
        dir_info = {
            'obj': root,
            'parent': os.path.dirname(root),
            'objtype': 'folder',
            'size': size
        }
        directory_info.append(dir_info)

        # Информация о файлах в текущей директории
        for file in files:
            file_path = os.path.join(root, file)
            file_info = {
                'obj': os.path.basename(file_path),
                'parent': root,
                'objtype': 'file',
                'size': os.path.getsize(file_path)
            }
            directory_info.append(file_info)
            size_dict[file_path] = file_info['size']

        # информация о вложенных директориях
        for d in dirs:
            dir_path = os.path.join(root, d)
            dir_info = {
                'obj': dir_path,
                'parent': root,
                'objtype': 'folder',
                'size': size
            }
            directory_info.append(dir_info)
            size_dict[dir_path] = dir_info['size']

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Pезультат в JSON файл
    json_path = os.path.join(output_folder, 'folder_info.json')
    with open(json_path, 'w') as json_file:
        json.dump(directory_info, json_file, indent=4)

    # Результат в CSV файл
    csv_path = os.path.join(output_folder, 'folder_info.csv')
    with open(csv_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['obj', 'parent', 'objtype', 'size'])
        writer.writeheader()
        writer.writerows(directory_info)

    # Результат в pickle файл
    pickle_path = os.path.join(output_folder, 'folder_info.pickle')
    with open(pickle_path, 'wb') as pickle_file:
        pickle.dump(directory_info, pickle_file)
