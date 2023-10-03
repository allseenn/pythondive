# 2. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.
from sys import argv
from serial.csv2json import csv_json
from serial.csv2pickle import pickler
from serial.json2csv import csv_gen
from serial.json2pickle import json_pickle
from serial.jsoner import json_gen
from serial.ls import ls_dir, dir_size


csv_json()
