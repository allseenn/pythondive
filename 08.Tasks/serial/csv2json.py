# Задание No4
# - Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# - Дополните id до 10 цифр незначащими нулями.
# - В именах первую букву сделайте прописной.
# - Добавьте поле хеш на основе имени и идентификатора.
# - Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# - Имя исходного и конечного файлов передавайте как аргументы
# функции.
import csv
import hashlib
import json
from sys import argv

if __name__ == '__main__':
    if len(argv) < 3:
        print(f"Example: python {argv[0]} input.csv output.json")
        exit(1)

def csv_json(csv_file, json_file):
    """
    Description: Function creates custom json file from custom csv file
    Arguments:
        csv_file - string input csv file name
        json_file - string output json file name
    Returns: String message
    """
    json_list = []
    with open(csv_file, 'r', encoding='utf-8') as input_file, open(json_file, 'w', newline='', encoding='utf-8') as output_file:
        csv_data = csv.reader(input_file, skipinitialspace=True)
        header = next(csv_data)
        for csv_list in csv_data:
            json_list.append(json.dumps({header[0]:csv_list[0], 
                            header[1]:f"{int(csv_list[1]):010d}", 
                            header[2]:csv_list[2].title(), 
                            "hash":hashlib.md5((csv_list[1]+csv_list[2]).encode()).hexdigest()}, ensure_ascii=False))
        output_file.writelines("[")
        output_file.write(",\n".join(json_list))
        output_file.writelines("]")
    return f"{json_file} with newline dicts created/updated"

if __name__ == '__main__':
    csv_json(argv[1], argv[2])

