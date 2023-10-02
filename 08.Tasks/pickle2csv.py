# Задание No6
# - Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# - Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
# - Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
import pickle
import csv
from sys import argv

if len(argv) < 2:
    print(f"Example: python {argv[0]} filename.pickle")
    exit(1)


with open(argv[1], "rb") as input, open(argv[1].replace(".pickle", ".csv"), "w", newline='') as output:
    dic_list = pickle.loads(input.read())
    csv_file = csv.DictWriter(output, [i for i in dic_list[0].keys()])
    csv_file.writeheader()
    csv_file.writerows(dic_list)

