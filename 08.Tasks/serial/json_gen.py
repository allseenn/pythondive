# Задача № 2
# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7). 
# После каждого ввода добавляйте новую информацию в JSON файл. 
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени. 
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа. 
# При перезапуске функции уже записанные в файл данные должны сохраняться.

import json
from sys import argv
from random import randint as ri

if __name__ == '__main__':
    if len(argv) < 2:
        print(f"Example: python {argv[0]} filename.json")
        exit(1)

def json_gen(json_file):
    """
    Description: Generates custom json file. Interacts with user with cycle asking him to enter data.
    Attributes: 
        json_file - string json filename
    Returns: string message
    """
    my_dict = {}
    try:
        with open(json_file, 'r', encoding='utf=8') as f:
            my_dict = json.load(f)     
    except:
        pass
    while True:
        name = input('Введите имя или q для выхода: ')
        if name == 'q':
            break
        level = input('Введите уровень: ')
        if 0 > int(level) > 7:
            print('Error')
        if level not in my_dict.keys():
            my_dict[level] = {}
        my_dict[level][ri(0, 10000)] = name
        print(my_dict)
    with open(json_file, 'w', encoding='utf=8') as f:
        json.dump(my_dict, f)
    return f"{json_file} created/updated"

if __name__ == '__main__':
    json_gen(argv[1])

