# Задание №1
# ✔ Напишите функцию, которая заполняет файл 
# (добавляет в конец) случайными парами чисел. 
# ✔ Первое число int, второе - float разделены вертикальной чертой. 
# ✔ Минимальное число - -1000, максимальное - +1000. 
# ✔ Количество строк и имя файла передаются как аргументы функции. 
import random as rnd

MIN_NUMBER = -1000
MAX_NUMBER = 1000

def fun_gen(num_str: int, file_name: str):
    with open(file_name, 'a', encoding='utf-8') as f:
        for _ in range(num_str):
            int_num = rnd.randint(MIN_NUMBER, MAX_NUMBER)
            float_num = rnd.uniform(MIN_NUMBER, MAX_NUMBER)
            f.write(f'{int_num}|{float_num:.2f}\n')

if __name__ =='__main__':
    fun_gen(5, 'new_file.txt')

