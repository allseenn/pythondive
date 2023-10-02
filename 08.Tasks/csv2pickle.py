# Задание No7
# - Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# - Распечатайте его как pickle строку.
import pickle
import csv
from sys import argv

if len(argv) < 2:
    print(f"Example: python {argv[0]} filename.csv")
    exit(1)

def pickler(csv_file):
    with open(csv_file, "r", newline='') as input:
        csv_list = list(csv.reader(input))
        print(pickle.dumps(csv_list))

if __name__ == '__main__':
    pickler(argv[1])
