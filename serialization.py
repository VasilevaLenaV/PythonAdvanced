import os
import json
import csv
import pickle
from typing import Callable


class SerializationFactory(object):
    def __init__(self):
        self.__directory_path = os.curdir
        self.__output_folder = 'output'
        self.__directory_info = []
        self.__size_dict = {}
        self.__root = '.'
        self.__size = 0

    @property
    def output_folder(self):
        return self.__output_folder

    @output_folder.setter
    def output_folder(self, output_folder):
        self.__output_folder = output_folder

    @property
    def directory_path(self):
        return self.__directory_path

    @directory_path.setter
    def directory_path(self, directory_path):
        self.__directory_path = directory_path

    def get_dirinfo(self, obj, parent, objtype, size):
        return {
            'obj': obj,
            'parent': os.path.dirname(parent),
            'objtype': objtype,
            'size': size
        }

    def read_curdir_info(self):
        self.__directory_info.append(self.get_dirinfo(self.__root, os.path.dirname(self.__root), 'folder', self.__size))

    def read_subdir_info(self, dirs):
        # информация о вложенных директориях
        for d in dirs:
            dir_path = os.path.join(self.__root, d)

            self.__directory_info.append(self.get_dirinfo(dir_path, self.__root, 'folder', self.__size))
            self.__size_dict[dir_path] = self.__size

    def read_files_info(self, files):
        for file in files:
            file_path = os.path.join(self.__root, file)
            dir_size = os.path.getsize(file_path)
            self.__directory_info.append(
                self.get_dirinfo(os.path.basename(file_path), self.__root, 'file', self.__size))
            self.__size_dict[file_path] = dir_size

    def folder_info(self):
        for root, dirs, files in os.walk(self.__directory_path):
            self.__root = root
            self.__size = sum(os.path.getsize(os.path.join(root, file)) for file in files)
            self.__size += sum(self.__size_dict.get(os.path.join(root, d), 0) for d in dirs)

            # Информация о текущей директории
            self.read_curdir_info()

            # Информация о файлах в текущей директории
            self.read_files_info(files)

            # информация о вложенных директориях
            self.read_subdir_info(dirs)

        if not os.path.exists(self.__output_folder):
            os.makedirs(self.__output_folder)

    def export_json(self):
        json_path = os.path.join(self.__output_folder, 'folder_info.json')
        with open(json_path, 'w') as json_file:
            json.dump(self.__directory_info, json_file, indent=4)

    def export_csv(self):
        csv_path = os.path.join(self.__output_folder, 'folder_info.csv')
        with open(csv_path, 'w', newline='', encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=['obj', 'parent', 'objtype', 'size'])
            writer.writeheader()
            writer.writerows(self.__directory_info)

    def export_pikle(self):
        pickle_path = os.path.join(self.__output_folder, 'folder_info.pickle')
        with open(pickle_path, 'wb') as pickle_file:
            pickle.dump(self.__directory_info, pickle_file)
