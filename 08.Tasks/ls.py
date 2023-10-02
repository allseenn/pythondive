# 1. Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.

# - Для дочерних объектов указывайте родительскую директорию.
# - Для каждого объекта укажите файл это или директория.
# - Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
import shutil
import json
import csv
import pickle
from sys import argv


if len(argv) < 2:
    argv.append(".")

def ls_dict(dirname):
    ls = []
    root = shutil.os.walk(dirname)
    for i in root:    
        dir = i[0]
        parent = shutil.os.path.dirname(i[0])
        size = shutil.os.path.getsize(dir)
        ls.append({"name":dir, "parent":parent, "type":"directory", "size":size})
        files = i[2]
        for file in files:
            size = shutil.os.path.getsize(dir+"/"+file)
            ls.append({"name":file, "parent":parent, "type":"file", "size":size})
    
    return ls

if __name__ == '__main__':
    dirname = argv[1]
    json_file = argv[1]+'.json'
    csv_file = argv[1]+'.csv'
    pickle_file = argv[1]+'.pickle'
    data = ls_dict(dirname)
    
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    with open(csv_file, 'w', encoding='utf-8') as f:        
        csv_writer = csv.DictWriter(f, [i for i in data[0]])
        csv_writer.writeheader()  
        csv_writer.writerows(data)

    with open(pickle_file, "wb") as f:
        pickle.dump(data, f)
    

        