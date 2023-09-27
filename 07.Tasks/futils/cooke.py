# Задание No4:
# - Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# - расширение
# - минимальная длина случайно сгенерированного имени, по умолчанию 6
# - максимальная длина случайно сгенерированного имени, по умолчанию 30
# - минимальное число случайных байт, записанных в файл, по умолчанию 256
# - максимальное число случайных байт, записанных в файл, по умолчанию 4096
# - количество файлов, по умолчанию 42
# - Имя файла и его размер должны быть в рамках переданного диапазона.
import random
import string
import shutil

def maker(extension, file_amount=42, dir=".", name_min=6, name_max=30, bytes_min=256, bytes_max=4096):
    """
    Create random_name.extension with random bytes inside
    ARGS: 
    - extension
    - name_min
    - name_max
    - content_min
    - content_max
    -files
    """
    if not shutil.os.path.exists(dir):
        shutil.os.mkdir(dir) 
    for _ in range(file_amount):  
        name = ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(name_min, name_max))
        bytes = random.randbytes(random.randint(bytes_min, bytes_max))
        with open(f"{dir}/{name}.{extension}", 'xb')as f:
            f.write(bytes)
              
# Задание No5:
# - Доработаем предыдущую задачу.
# - Создайте новую функцию которая генерирует файлы с разными расширениями.
# - Расширения и количество файлов функция принимает в качестве параметров.
# - Количество переданных расширений может быть любым.
# - Количество файлов для каждого расширения различно.
# - Внутри используйте вызов функции из прошлой задачи.
    

# Задание No6:
# - Дорабатываем функции из предыдущих задач.
# - Генерируйте файлы в указанную директорию — отдельный параметр функции.
# - Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# - Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

def filer(**kwargs) -> list:
    dir=kwargs.pop("dir")
    for k, v in kwargs.items():
        maker(k, v, dir)
    return list(shutil.os.walk(dir))[0][2]
    
# Задание No7:
# - Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# - Каждая группа включает файлы с несколькими расширениями.
# - В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import pathlib

def sorter(dirname):
    file_list = {}

    # Создаем папки, если они не существуют
    for folder in ["video", "img", "text"]:
        folder_path = pathlib.Path(dirname) / folder
        folder_path.mkdir(exist_ok=True)

    # Перемещаем файлы в соответствующие папки
    for file_path in pathlib.Path(dirname).glob("*"):
        if file_path.is_file():
            if file_path.suffix == ".avi":
                dest_folder = "video"
            elif file_path.suffix == ".jpg":
                dest_folder = "img"
            elif file_path.suffix == ".txt":
                dest_folder = "text"
            else:
                continue  # Пропускаем файлы, которые не подходят под расширения

            dest_path = pathlib.Path(dirname) / dest_folder / file_path.name
            file_path.rename(dest_path)

    # Собираем список файлов в каждой папке
    return list(pathlib.os.walk(dirname))[1:]


if __name__ =='__main__':
    print(*filer(avi=2, jpg=2, txt=2, dir='tmp'), sep="\n")
    print(*sorter("tmp"), sep="\n")
