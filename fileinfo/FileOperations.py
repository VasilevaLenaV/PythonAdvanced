def save_to_file(file_info_list):
    with open("file_info.txt", "w", encoding="utf-8") as file:
        for file_info in file_info_list:
            file.write(f"Имя: {file_info.name}\n")
            file.write(f"Расширение: {file_info.extension}\n")
            file.write(f"Директория: {file_info.is_dir}\n")
            file.write(f"Родительская директория: {file_info.parent_dir}\n")
            file.write("\n")
