# 2. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.
from serial.json_gen import json_gen
from serial.json2csv import csv_gen
from serial.csv2json import csv_json
from serial.json2pickle import json_pickle
from serial.pickle2csv import pickle_csv
from serial.csv2pickle import pickler
from serial.ls import ls_dir, dir_size

input("Запуск всех задач из 8 домашки и семинара. Enter для продолжения")
print(json_gen("task02.json")) # 2 sem
input("Задача 2 из 8 семинара выполнена. Enter для продолжения")
print(csv_gen("task02.json", "task03.csv")) # 3 sem
input("Задача 3 из 8 семинара выполнена. Enter для продолжения")
print(csv_json("task03.csv", "task04.json")) # 4 sem
input("Задача 4 из 8 семинара выполнена. Enter для продолжения")
print(json_pickle(".")) # 5 sem
input("Задача 5 из 8 семинара выполнена. Enter для продолжения")
print(pickle_csv("task04.pickle")) # 6 sem
input("Задача 6 из 8 семинара выполнена. Enter для продолжения")
pickler("task03.csv") # 7 sem
input("Задача 7 из 8 семинара выполнена. Enter для продолжения")
print(ls_dir(".")) # 1 HW
print("Задача 1 из 8 домашки выполнена!")
input("Задача 2 из 8 домашки - это данный файл main.py. Enter для выхода")


