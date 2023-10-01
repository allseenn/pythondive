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
if len(argv) < 2:
    print(f"Example: python {argv[0]} filename.json")
    exit(1)

def json_gen(json_file):
    my_dict = {}

    new_json = json.dumps(my_dict)

    def my_json(my_dict):
    
        while True:
            name = input('Введите имя: ')
            if name == 'q':
                break
            level = input('Введите уровень: ')
            if 0 > int(level) > 7:
                print('Error')
            if level not in my_dict.keys():
                my_dict[level] = {}
            my_dict[level][ri(0, 10000)] = name
            print(my_dict)


    try:
        with open(json_file, 'r', encoding='utf=8') as f:
            my_dict = json.load(f)     
    except:
        pass
    finally:
        my_json(my_dict)
        with open(json_file, 'w', encoding='utf=8') as f:
            json.dump(my_dict, f)
    return "JSON file updated"


if __name__ == '__main__':
    json_gen(argv[1])