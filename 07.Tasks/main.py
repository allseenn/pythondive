# 2. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
from sys import argv

if len(argv)==3:
    source = argv[1]
    destination = argv[2]
    print(source, destination)
else:
    print(f"Example: python3 {argv[0]} ./src_dir/*.ext1 ./dest_dir/*.ext2")