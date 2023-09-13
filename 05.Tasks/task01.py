# 1. Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
def path_parse(str):
    try: 
        full_path, file_extension = str.split(".")
    except:
        return "Not", "correct", "path"

    if full_path.count("\\") > 0:
        *file_path, file_name = full_path.split("\\")
        file_str = "\\".join(file_path)
    else:
        *file_path, file_name = full_path.split("/")
        file_str = "/".join(file_path)
    return file_str, file_name, file_extension

print(*path_parse(input("Enter like /full/path/to/file.ext: ")), sep="\n")