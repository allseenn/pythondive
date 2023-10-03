# Задание No5
# - Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.
import shutil
import json
import pickle
from sys import argv

if len(argv) < 2:
    argv.append(".")
    

def json_pickle(dir_name):
    """
    Function: Convert all json files to pickle format inside given directory
    Arguments: 
        dir_name - string dir name
    Returns: string message
    """
    file_list = list(shutil.os.walk(dir_name))
    for i in file_list[0][2]:
        if ".json" in i:
            with open(dir_name+"/"+i, "r") as input, open(dir_name+"/"+i.replace(".json", ".pickle"), "wb") as output:
                json_data = json.load(input)
                pickle.dump(json_data, output)
    return f"inside {dir_name} all csv files converted to pickle format"


if __name__ == '__main__':
    json_pickle(argv[1])