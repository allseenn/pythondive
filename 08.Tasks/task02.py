# Задача № 2
# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7). 
# После каждого ввода добавляйте новую информацию в JSON файл. 
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени. 
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа. 
# При перезапуске функции уже записанные в файл данные должны сохраняться.

import json
from sys import argv
if len(argv) < 2:
    print(f"Example: {argv[0]} filename.json")
    exit(1)

my_dict = {}

new_json = json.dumps(my_dict)

def my_json(my_dict):
 
    id = 4
    while True:
        id += 1
        name = input('Введите имя: ')
        if name == 'q':
            break
        level = input('Введите уровень: ')
        if int(level) < 0 and int(level) >7:
            print('Error')
        if level not in my_dict.keys():
            my_dict[level] = {}
        my_dict[level][id] = name
        print(my_dict)


try:
    with open(argv[1], 'r', encoding='utf=8') as f:
        my_dict = json.load(f)     
except:
    pass
finally:
    my_json(my_dict)
    with open(argv[1], 'w', encoding='utf=8') as f:
        json.dump(my_dict, f)
