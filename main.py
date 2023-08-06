# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# * имя файла без расширения или название каталога,
# * расширение, если это файл,
# * флаг каталога,
# * название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

import argparse
import logging
from fileinfo import process_directory, save_to_file

logging.basicConfig(filename='file_info.log', level=logging.INFO)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", help="Путь до директории")
    args = parser.parse_args()

    directory = args.directory

    file_info_list, logging = process_directory(directory, logging)
    save_to_file(file_info_list)

    logging.info("Информацию о содержимом сохранена в файл 'file_info.txt'")
