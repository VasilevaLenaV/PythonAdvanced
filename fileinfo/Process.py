import os
from collections import namedtuple

FileInfo = namedtuple("FileInfo", ["name", "extension", "is_dir", "parent_dir"])


def process_directory(directory, logging):
    file_info_list = []
    for entry in os.scandir(directory):
        name = os.path.splitext(entry.name)[0]
        extension = os.path.splitext(entry.name)[1][1:]
        is_dir = entry.is_dir()
        parent_dir = os.path.dirname(entry.path)
        file_info = FileInfo(name, extension, is_dir, parent_dir)
        file_info_list.append(file_info)
        logging.info(f"Обработано: {file_info}")
    return file_info_list, logging
